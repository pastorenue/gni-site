from django.conf.urls import include, url
from .views import *

urlpatterns = [
    url(r'^new$', new_contact, name="new-contact"),
]