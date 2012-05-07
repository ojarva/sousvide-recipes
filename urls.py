from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^cachefail/', TemplateView.as_view(template_name="cachefail.html")),
    url(r'accounts/login/$', 'django.contrib.auth.views.login', {"template_name": "login.html"}, name="login"),
    url(r'accounts/logout/$', 'django.contrib.auth.views.logout', {"template_name": "logout.html"}, name="logout"),
    url(r'accounts/profile/$', 'django.views.generic.simple.redirect_to', {"url": "/recipes/"}),
    url(r'^', include("recipes.urls")),
)

