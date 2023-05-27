from django.db import models


class Article(models.Model):
    # fields
    title = models.CharField('Title', max_length=256)
    content = models.TextField('Content')
    published = models.BooleanField('Published', default=False)
    created_at = models.DateTimeField('Created At', auto_now_add=True)
    updated_at = models.DateTimeField('Updated At', auto_now=True)

    # meta
    class Meta:
        ordering = ('-created_at',)

    # methods
    def __str__(self):
        return self.title

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    @classmethod
    def get_published(cls, published):
        published = str(published).lower() in ('true', 'yes')
        return cls.objects.filter(published=published)
