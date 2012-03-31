from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView
from django.views.generic.base import View
from django.core.cache import cache

from .models import Article


class OnlyStaffMixin(View):
    """Requires a user be authenticated and have staff status to look at the view."""
    forbidden_message = "You cannot do that."
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return HttpResponseForbidden(self.forbidden_message)
        return super(OnlyStaffMixin, self).dispatch(request, *args, **kwargs)
    
class CacheDetailView(DetailView):
    """This caches the object for a detailed view.
    Note: you must set the context_object_name member or this will not function properly."""
    cache_timeout = 300
    
    def get_object(self, queryset=None):
        # Assure they set this so the cache isn't corrupt
        if not self.context_object_name: return super(CacheDetailView, self).get_object(queryset)
        
        key = (self.context_object_name, self.kwargs.get('pk', None), self.kwargs.get('slug', None))
        obj = cache.get(key)
        if obj: return obj
        obj = super(CacheDetailView, self).get_object(queryset)
        cache.set(key, obj, self.cache_timeout)
        return obj


class ArticleListView(ListView):
    model = Article
    
class ArticleDetailView(CacheDetailView):
    model = Article
    context_object_name = "article"
    
class ArticleCreateView(OnlyStaffMixin, CreateView):
    model = Article
    forbidden_message = "Only staff can blog."
    
class ArticleUpdateView(OnlyStaffMixin, UpdateView):
    model = Article
    forbidden_message = "Only staff can blog."

class ArticleDeleteView(OnlyStaffMixin, DeleteView):
    model = Article
    forbidden_message = "Only staff can blog."
    
    def get_success_url(self):
        return reverse("blog")
