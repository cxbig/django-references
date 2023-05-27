# Generated by Django 4.2.1 on 2023-05-27 16:16

import random

from django.db import migrations, models


def add_initial_articles(apps, schema_editor):
    article_model = apps.get_model('articles', 'Article')
    for i in range(100):
        padding_num = str(i).rjust(3, '0')
        title = f'Title {padding_num}'
        content = f'Content {padding_num}'
        published = bool(random.getrandbits(1))
        article_model.objects.create(title=title, content=content, published=published)


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('content', models.TextField(verbose_name='Content')),
                ('published', models.BooleanField(default=False, verbose_name='Published')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.RunPython(add_initial_articles, reverse_code=migrations.RunPython.noop),
    ]
