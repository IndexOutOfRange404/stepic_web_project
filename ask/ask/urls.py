from django.conf.urls import patterns, include, url

from django.contrib import admin

import qa.views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', qa.views.new),
    url(r'^login/$', qa.views.login),
    url(r'^signup/$', qa.views.signup),
    url(r'^question/(?P<question_id>\d+)/$', qa.views.question),
    url(r'^ask/$', qa.views.ask),
    url(r'^popular/$', qa.views.popular),
    url(r'^new/$', qa.views.new),
)