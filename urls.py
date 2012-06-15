from django.conf.urls.defaults import patterns, include, url
from imgup.views import upload_file
from registration.views import register, logout_user, mylogin
from userprofile.views import get_images
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'imgup.views.home', name='home'),
    # url(r'^imgup/', include('imgup.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',upload_file),
    url(r'^register/$',register),
    url(r'^logout/$',logout_user),
    url(r'^login/$',mylogin),
    url(r'^my-images/$',get_images),
)
