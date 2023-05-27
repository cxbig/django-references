from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Article


def normal_view(request):
    published = request.GET.get('published', None)
    if published is None:
        articles = Article.get_all()
    else:
        articles = Article.get_published(published)

    page = request.GET.get('page', 1)
    paginator = Paginator(articles, 10)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(request, 'articles/normal_view.html', {
        'page_title': 'Normal View',
        'articles': articles,
    })


class ArticleListView(ListView):
    model = Article
    template_name = 'articles/list_view.html'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['page_title'] = 'List view'

        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        published = self.request.GET.get('published', None)
        if published is not None:
            queryset = Article.get_published(published)

        return queryset
