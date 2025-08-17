from django.contrib import admin
from .models import LandingPageEntry

# Register your models here.

class LandingPageEntryAdmin(admin.ModelAdmin):
    list_display=("name","email","timestamp","updated", "notes","notes_by")
    search_fields=["name", "email"]
    read_only_fields=["id","name","email","timestamp"]

    list_filter=["active","timestamp"]


admin.site.register(LandingPageEntry,LandingPageEntryAdmin)
