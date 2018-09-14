from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=255, null=True)
    organization = models.CharField(max_length=255, null=True, blank=True)
    message = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}-{}".format(self.full_name, self.email)
    
