from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^contact/$', views.contact_us, name='contact'),
    url(r'^ajax/contact-us/$', views.contact_us_ajax, name='contact_ajax'),
]
