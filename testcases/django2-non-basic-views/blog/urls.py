from django.urls import path
from django.views.generic import ListView
from .models import Article

from .views import (

    ArticleListViewStartsWith,
    ArticleCreateView,
    ArticleDeleteView,
    ArticleDetailView,
    ArticleListView,
    ArticleUpdateView,
    ArticleUpdateContextDataView,
   

)

app_name = 'articles'
urlpatterns = [

    path('', ArticleListView.as_view(), name='article-list'),
    path('<str:title>/article_starts_with/',ArticleListViewStartsWith.as_view(), name='article-list-starts-with'),
    # Attack.Payload  curl -X GET  'http://localhost:8000/blog/blog1/article_model_list/'
    path('<title>/article_model_list/',ListView.as_view(model=Article, context_object_name="articles"), name='article-list-model-list'), # uses default template naming convention
    #path('<title>/article_model_list/',ListView.as_view(model=Article.objects.filter(title__startswith='%(title)s')), name='article-list'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),

    #path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'),
    path('<str:title>/', ArticleDetailView.as_view(), name='article-detail'),
    path('<str:title>/update/', ArticleUpdateView.as_view(), name='article-update'),
    path('<str:title>/update_context_data/',ArticleUpdateContextDataView.as_view(),name='article-update'),
    #path('<int:id>/update/', ArticleUpdateView.as_view(), name='article-update'),
    #path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
    path('<str:title>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
]
