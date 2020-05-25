from django.contrib import admin
from django.urls import path
from . import views
from project1 import views as project1_views
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('textutiles', views.textutiles, name='textutiles'),
    path('analyze', views.analyze, name='analyze'),
    path('codebeautifier', views.codebeautifier, name='codebeautifier'),

    url(r'^mergepdf$', project1_views.mergepdf, name="mergepdf"),
    url(r'^lock$', project1_views.lock, name="lock"),
    url(r'^unlock$', project1_views.unlock, name="unlock"),
    url(r'^compress$', project1_views.compress, name="compress"),



    # urls(r'^dashboard/$', 'project1.views.dashboard',name='dashboard'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
