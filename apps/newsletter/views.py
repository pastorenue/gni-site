from django.shortcuts import render, redirect, get_object_or_404
from .models import Newsletter, Recruitment
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login, authenticate, logout


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
        first_name = params.get('f_name')
        last_name = params.get('l_name')
        gender = params.get('gender')
        email = params.get('email')
        phone = params.get('phone')
        cv = request.FILES.get('cv')
        dob = params.get('dob')

        payload = {
            'gender': gender, 
            'phone': phone, 
            'cv': cv, 
        }
        
        try:
            user = User.objects.create_user(last_name = last_name, 
                                    first_name=first_name, 
                                    email=email, 
                                    password=email, 
                                    username=email)
            recruit = Recruitment(**payload)
            recruit.user = user
            recruit.job_status = 2
            recruit.save()
            # Login the user
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)

            messages.success(request, "Thank you for registering with GNI Job Board. Your credentials is been reviewed. \
                                You will be notified shortly")
            return redirect("new-recruit")
        except Exception as e:
            messages.error(request, e)
            return redirect('new-recruit')
    return render(request, 'dubai_jobs.html', {})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'password_change.html', {
        'form': form
    })


@login_required
def dashboard(request):
    template_name='dashboard.html'
    user = request.user
    recruit = get_object_or_404(Recruitment, user=user)
    return render(request, template_name, {'recruit': recruit})
 