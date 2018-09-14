from django.db import models

# Create your models here.
class Newsletter(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=255, null=True, blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.email)
    