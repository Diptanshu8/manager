from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('user_managent.view',
    # Examples:
    # url(r'^$', 'manager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$','index',name='user.index')
)
