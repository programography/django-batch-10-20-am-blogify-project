from django.db import models

# Create your models here.

class contactus(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    phone_number = models.IntegerField()
    dob = models.CharField(max_length=150)
    gender = models.CharField(max_length=150, default="nice")
    message = models.TextField()
    q_image = models.ImageField(upload_to="user_quieres", null = True, blank = True)
    