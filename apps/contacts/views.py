from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import Contact
try:
    import json
except:
    import simplejson as json


def new_contact(request):
    data = {}
    if request.method == "POST":
        params = request.POST
        email = params.get('email')
        full_name = params.get('full_name')
        organization = params.get('organization')
        message = params.get('message')

        payload = {
            "email": email,
            "full_name": full_name,
            "organization": organization,
            "message": message
        }
        contact = Contact.objects.create(**payload)
        messages.success(request, "Thank you for reaching out to us. We wil get back to you.")
    data["message"] = "Thank you for reaching out to us. We wil get back to you."
    #return HttpResponse(json.dumps(data), content_type="application/json")
    return HttpResponseRedirect(reverse("contact-us"))