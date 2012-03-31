from django.conf.urls.defaults import patterns, include, url

from .views import ArticleDetailView, ArticleListView, ArticleUpdateView, ArticleCreateView, ArticleDeleteView

urlpatterns = patterns('',
   url(r'^$', ArticleListView.as_view(), name='blog'),
   url(r'^create/$', ArticleCreateView.as_view(), name='create_article'),
   url(r'^(?P<slug>[\w\._-]+)/$', ArticleDetailView.as_view(), name='article'),
   url(r'^(?P<slug>[\w\._-]+)/edit/$', ArticleUpdateView.as_view(), name='edit_article'),
   url(r'^(?P<slug>[\w\._-]+)/delete/$', ArticleDeleteView.as_view(), name='delete_article'),
)
