from puput.models import BlogPage
from django.conf import settings


def first_post(request):
    return {'first_post' : BlogPage.objects.first()}


def static_number(request):
    return {'static_number': str(settings.STATIC_NUMBER)}