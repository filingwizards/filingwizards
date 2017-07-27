import json

from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render

from .forms import ContactForm


def contact_us(request):
    form = ContactForm(request.POST or None)

    return render(request, 'contact/contact.html', {'form': form})

def contact_us_ajax(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        save_form = form.save(commit=False)
        save_form.subject = save_form.subject or 'Contact message on Street Corner Resources Website'
        save_form.save()

        response_data = {'status': 'success'}
        return HttpResponse(json.dumps(response_data), content_type='application/json')
    else:
        response_data = {'status': 'error'}
        return HttpResponseBadRequest(json.dumps(response_data), content_type='application/json')