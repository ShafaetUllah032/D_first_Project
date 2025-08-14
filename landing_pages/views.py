#from django.http import HttpResponse
from django.shortcuts import render
from .forms import LandingPageEntryModelFrom as LandingPageForm
from .models import LandingPageEntry 



def home_page(request,*args, **kwargs):

    title="Welcome"
    form = LandingPageForm(request.POST or None)
    if form.is_valid():
        obj=form.save()
        # print(form.cleaned_data)
        # name=form.cleaned_data.get("name")
        # email=form.cleaned_data.get("email")
        # LandingPageEntry.objects.create(
        #     name=name,
        #     email=email
        # )
       # obj=LandingPageEntry()
        #obj.email=email
        # obj.save()
        form=LandingPageForm()

    context={
        "title": title,
        "form": form,
    }
    return render(request, "landing_pages/home.html",context)

def random_page(request,*args, **kwargs):
    title="Random page"
    context={
        "title": title
    }
    return render(request, "abc.html",context)






def landing_page_entry_list_view(request,*args, **kwargs):
    

    qs=LandingPageEntry.objects.all()
    context={
        "object_list":qs,
    }
    return render(request, "landing_pages/list.html",context)


