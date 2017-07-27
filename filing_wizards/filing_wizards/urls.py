from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from search import views as search_views
from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^django-admin/', include(admin.site.urls)),

    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),


    url(r'^search/$', search_views.search, name='search'),

    url(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    url(r'^services/$', TemplateView.as_view(template_name='services.html'), name='services'),
    url(r'^llc-services/$', TemplateView.as_view(template_name='llc-services.html'), name='llc-services'),
    url(r'^faqs/$', TemplateView.as_view(template_name='faqs.html'), name='faqs'),
    url(r'^terms/$', TemplateView.as_view(template_name='terms.html'), name='terms'),
    url(r'^privacy-policy/$', TemplateView.as_view(template_name='privacy-policy.html'), name='privacy-policy'),
    url(r'^disclaimer/$', TemplateView.as_view(template_name='disclaimer.html'), name='disclaimer'),

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:

    url(r'', include('contact.urls')),
    url(r'', include('puput.urls')),
    url(r'', include(wagtail_urls)),

    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    url(r'^pages/', include(wagtail_urls)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
