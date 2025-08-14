from django import forms
from .models import LandingPageEntry


class LandingPageEntryModelFrom(forms.ModelForm):

    # name=forms.CharField(required=False)
    # email= forms.EmailField() 
    email2=forms.EmailField(label="Confirm email")

    class Meta:
        model = LandingPageEntry
        fields=["name","email"]


    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        print(self.fields)

        for field in self.fields:
            print(field)
            default_css_class= 'form-control'

            new_attrs={
                "class":default_css_class,
                "id":f"{field}",
                "placeholder":f"Your {field}"
            }

            if field == "email2":
                new_attrs["placeholder"]=f"Your confirm email"

            self.fields[field].widget.attrs.update(new_attrs)



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

# class LandingPageForm(forms.Form):

#     name=forms.CharField(required=False)
#     email= forms.EmailField() 
#     email2=forms.EmailField(label="Confirm email")


#     def __init__(self, *args, **kwargs):
#         super().__init__(*args,**kwargs)
#         print(self.fields)

#         for field in self.fields:
#             print(field)
#             default_css_class= 'form-control'

#             new_attrs={
#                 "class":default_css_class,
#                 "id":f"{field}",
#                 "placeholder":f"Your {field}"
#             }

#             if field == "email2":
#                 new_attrs["placeholder"]=f"Your confirm email"

#             self.fields[field].widget.attrs.update(new_attrs)



#     def clean(self):
#         data=self.cleaned_data
#         email=data.get("email")
#         email2=data.get("email2")
#         if email!=email2:
#             self.add_error("email", "Fucker give the same email")

#         return data

#     def clean_email(self):
#         email=self.cleaned_data.get("email")
#         if email.endswith("gmail.com"):
#             #self.add_error("email", "you can not use gmail")
#             raise forms.ValidationError("you cann't use gmail")
#         return email
