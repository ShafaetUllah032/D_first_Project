from django.conf import settings
from django.db import models

User=settings.AUTH_USER_MODEL

# Create your models here.
class LandingPageEntry(models.Model):

    name=models.CharField(max_length=20, blank=True, null=True )
    email= models.EmailField() 
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
    notes_by = models.ForeignKey(User,blank=True, null=True, on_delete=models.SET_NULL)
    note_first_addeed=models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    updated= models.DateTimeField(auto_now=True) 


    def __str__(self):
        return f"{self.email}"
     

    def get_absolute_url(self):
        return f"/entries/{self.id}"
     