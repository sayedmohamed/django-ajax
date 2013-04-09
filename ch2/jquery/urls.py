from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'jquery.views.ch1'),
    url(r'^show-params/$', 'jquery.views.show_params'),

    url(r'^ch2/$', 'jquery.views.ch2'),
    url(r'^nums/$', 'jquery.views.nums'),
    # url(r'^jquery/', include('jquery.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
