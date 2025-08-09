#from django.http import HttpResponse
from django.shortcuts import render
from .forms import LandingPageForm



def home_page(request,*args, **kwargs):

    

    title="Welcome"
    form = LandingPageForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form=LandingPageForm()

    context={
        "title": title,
        "form": form,
    }
    return render(request, "home.html",context)

def random_page(request,*args, **kwargs):
    title="Random page"
    context={
        "title": title
    }
    return render(request, "abc.html",context)
