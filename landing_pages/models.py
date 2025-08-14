from django.db import models

# Create your models here.
class LandingPageEntry(models.Model):

    name=models.CharField(max_length=20, blank=True, null=True )
    email= models.EmailField() 
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f"{self.email}"
    