from django.db import models

# Create your models here.
class Newsletter(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=255, null=True, blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.email)

INACTIVE, INITIATED, PROCESSING, ACTIVE = range(0,4)
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
    full_name = models.CharField(max_length=255, null=True)
    gender = models.CharField(max_length=10, choices=GENDER, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=15, null=True)
    job_status = models.CharField(max_length=1, choices=JOB_STATUS, default=0)
    cv = models.FileField(upload_to='uploads')
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s (%s)" % (self.full_name, self.email)
 