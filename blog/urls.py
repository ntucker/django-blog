from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from bloggy.views import ArticleListView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', ArticleListView.as_view(), name='home'),
    url(r'^blog/', include('bloggy.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^account/', include('recaptcha_form.registration_backend.urls')),
    url(r'^tinymce/', include('tinymce.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
if settings.SERVE_MEDIA:
    urlpatterns += patterns("",
        url(r"", include("staticfiles.urls")),
    )
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)