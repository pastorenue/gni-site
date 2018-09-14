from django.shortcuts import render, redirect
from .models import Newsletter
from django.contrib import messages

def new_newsletter(request):
    if request.method == "POST":
        params = request.POST
        email = params.get("email")
        full_name = params.get("full_name", "Visitor")

        payload = {
            "email": email,
            "full_name": full_name
        }
        newsletter = Newsletter.objects.create(**payload)
        messages.success(request, "You have successfully signed up for GNI newsletters")
    return redirect("index")
