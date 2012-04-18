from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),

	url(r'^$', 'main.views.index'),
	url(r'^contact$', 'main.views.contact'),

	(r'^user/', include('registration.urls')),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^static/(?P<path>.*)$',
			'django.views.static.serve',
			{'document_root': settings.STATIC_ROOT}),
	)

	urlpatterns += patterns('',
		(r'^media/(?P<path>.*)$',
			'django.views.static.serve',
			{'document_root': settings.MEDIA_ROOT}),
	)
