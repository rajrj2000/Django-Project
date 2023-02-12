from django.db import models

# Create your models here.
class Enquiry(models.Model):
    name=models.CharField(max_length=50)
    phone=models.IntegerField()
    mailid=models.EmailField()
