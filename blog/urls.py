from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),

        url(r'^contact/$', views.contact ,name='contact'),
        url(r'^contact_messages/$', views.contact_messages,name='contact_messages'),

        url(r'^categories/$', views.categories, name='categories'),
        url(r'^feedback_form/$', views.feedback_form, name='feedback_form'),
        url(r'^comment_form/$', views.comment_form, name='comment_form'),
        url(r'^feedback/$', views.feedback, name='feedback'),
        url(r'^category/add_category/$', views.add_category, name='add_category'),
        url(r'^category/(?P<category_name_slug>[-\w]+)/$', views.category, name='category'),
        url(r'^tag/(?P<tag_name_slug>[a-zA-Z0-9_.-]+)/$', views.tag, name='tag'),
        url(r'^add_post/$', views.add_post, name='add_post'),
        url(r'^(?P<blog_post_slug>[-\w]+)/$', views.blog_post, name='blog_post'),
)