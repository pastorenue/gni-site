"""gni_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView
from newsletter.views import new_recruit, dashboard
from django.contrib.auth import views as auth_views
from newsletter.views import change_password
from django.views.static import serve
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),
    url(r'^services$', TemplateView.as_view(template_name="services.html"), name="services"),
    url(r'^events-and-conferences$', TemplateView.as_view(template_name="events.html"), name="events"),
    url(r'^jobs$', new_recruit, name="new-recruit"),
    url(r'^my-status$', dashboard, name="dashboard"),
    url(r'^contact-us$', TemplateView.as_view(template_name="contact.html"), name="contact-us"),
    url(r'^president-speech$', TemplateView.as_view(template_name="speech.html"), name="speech"),
    url(r'^newsletters/', include('newsletter.urls', namespace='newsletters')),
    url(r'^contact-us/', include('contacts.urls', namespace='contacts')),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += [
    url(r'^auth/login$', auth_views.LoginView.as_view(template_name='sign_in.html'), name='login'),
    url(r'^auth/password_change$', change_password, name='password_change'),
    url(r'^auth/password_change/done$', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    url(r'^auth/logout/$', auth_views.LogoutView.as_view(), name='logout'),
]
