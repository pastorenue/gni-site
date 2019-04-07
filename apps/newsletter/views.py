from django.shortcuts import render, redirect
from .models import Newsletter, Recruitment
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


def new_recruit(request):
    if request.method == 'POST':
        params = request.POST
        full_name = params.get('f_name')
        gender = params.get('gender')
        email = params.get('email')
        phone = params.get('phone')
        cv = request.FILES.get('cv')
        dob = params.get('dob')

        payload = {
            'full_name': full_name,
            'gender': gender, 
            'email': email, 
            'phone': phone, 
            'cv': cv, 
        }
        
        try:
            import pdb; pdb.set_trace()
            recruit = Recruitment.objects.create(**payload)
            messages.success(request, "Thank you for registering with GNI Job Board. Your credentials is been reviewed. \
                                You will be notified shortly")
            return redirect("new-recruit")
        except Exception as e:
            messages.error(request, e)
            return redirect('new-recruit')
    return render(request, 'dubai_jobs.html', {})
