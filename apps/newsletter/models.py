from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Newsletter(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=255, null=True, blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.email)

INACTIVE, INITIATED, PROCESSING, ACTIVE = range(1,5)
JOB_STATUS = (
    (INACTIVE, 'Inactive'),
    (INITIATED, 'Initiated'),
    (PROCESSING, 'Processing'),
    (ACTIVE, 'Active'),
)

GENDER = (
    ('M', 'Male'),
    ('F', 'Female')
)
class Recruitment(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=GENDER, null=True)
    phone = models.CharField(max_length=15, null=True)
    job_status = models.PositiveIntegerField(choices=JOB_STATUS, default=1)
    cv = models.FileField(upload_to='uploads')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % (self.user)
    
    def get_status(self):
        status = dict(JOB_STATUS)
        return status[self.job_status]
 