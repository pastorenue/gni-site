from django.conf.urls import include, url
from .views import *

urlpatterns = [
    url(r"^newsletter-signup$", new_newsletter, name="newsletter-signup"),
]