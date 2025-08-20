from django.contrib import messages

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .forms import LandingPageEntryModelFrom as LandingPageForm , EntryNotesModelForm
from .models import LandingPageEntry 



def home_page(request,*args, **kwargs):
    messages.success(request,"Hey , done good job selecting this site!")
    title="Welcome"
    form = LandingPageForm(request.POST or None)
    did_submit = False
    if form.is_valid():
        form.save()
        messages.success(request,"Thanks for visiting our site!")
        request.session['did_submit'] = True
        return HttpResponseRedirect("/")      
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




# @login_required
# @user_passes_test(lambda u: u.is_staff)

def landing_page_entry_list_view(request,*args, **kwargs):
     
    user=request.user
    if not user.is_authenticated:
        return HttpResponse("Yous must be logged in to view this page.",status=404)
    if not user.is_staff:
        return HttpResponse("You are not authorized to view this page.", status=404)

    qs=LandingPageEntry.objects.all()
    context={
        "object_list":qs,
    }
    return render(request, "landing_pages/list.html",context)

def landing_page_entry_detail_view(request,*args, **kwargs):
     
    user=request.user
    if not user.is_authenticated:
        return HttpResponse("Yous must be logged in to view this page.",status=404)
    if not user.is_staff:
        return HttpResponse("You are not authorized to view this page.", status=404)

    obj=get_object_or_404(LandingPageEntry, id=kwargs.get("id"))

    form =EntryNotesModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        obj=form.save(commit=False)
        if not obj.notes_by:
            obj.note_first_addeed = timezone.now()
        obj.notes_by=user
        obj.save()
        messages.success(request,f"Entry {obj.id} Updated successfully!", extra_tags="alert alert-success")
        return HttpResponse(obj.get_absolute_url())

    context={
        "object":obj,
        "form": form,
    }
    return render(request, "landing_pages/detail.html",context)

def entry_list_notes_view(request,*args, **kwargs):
    

    qs=LandingPageEntry.objects.none()
    user=request.user
    if user.is_authenticated:
        qs=LandingPageEntry.objects.filter(notes_by=user)
    context={
        "object_list":qs,
    }
    return render(request, "landing_pages/list.html",context)


