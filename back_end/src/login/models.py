from django.db import models

# Create your models here.
class AdminRegistration(models.Model):
	user_name = models.CharField(max_length=128, blank=False, null=True)
	user_pwd  = models.CharField(max_length=256, blank=False, null=True)
	user_email= models.EmailField(unique=True, blank=False, null=True)

    

