from django import forms
from . import mixins
from .models import LandingPageEntry


class EntryNotesModelForm(mixins.BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = LandingPageEntry
        fields =["name","email","notes"]




class LandingPageEntryModelFrom(mixins.BootstrapFormMixin,forms.ModelForm):

    # name=forms.CharField(required=False)
    # email= forms.EmailField() 
    email2=forms.EmailField(label="Confirm email")

    class Meta:
        model = LandingPageEntry
        fields=["name","email"]

    def clean(self):
        data=self.cleaned_data
        email=data.get("email")
        email2=data.get("email2")
        if email!=email2:
            self.add_error("email", "Fucker give the same email")

        return data

    def clean_email(self):
        email=self.cleaned_data.get("email")
        if email.endswith("gmail.com"):
            #self.add_error("email", "you can not use gmail")
            raise forms.ValidationError("you cann't use gmail")
        return email

class LandingPageForm(mixins.BootstrapFormMixin,forms.Form):

    name=forms.CharField(required=False)
    email= forms.EmailField() 
    email2=forms.EmailField(label="Confirm email")


    def clean(self):
        data=self.cleaned_data
        email=data.get("email")
        email2=data.get("email2")
        if email!=email2:
            self.add_error("email", "Fucker give the same email")

        return data

    def clean_email(self):
        email=self.cleaned_data.get("email")
        if email.endswith("gmail.com"):
            #self.add_error("email", "you can not use gmail")
            raise forms.ValidationError("you cann't use gmail")
        return email
