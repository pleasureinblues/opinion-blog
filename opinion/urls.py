from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog import views

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'views.home', name='home'),
    #url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^tinymce/', include('tinymce.urls')),
    (r'^accounts/', include('registration.backends.simple.urls')),

)
