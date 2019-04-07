from django.contrib import admin
from .models import Newsletter, Recruitment

# Register your models here.
@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    display = ('full_name', 'full_name', 'time_stamp')

@admin.register(Recruitment)
class RecruitmentAdmin(admin.ModelAdmin):
    display = ('user', 'gender', 'date_created')