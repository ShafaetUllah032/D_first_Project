from django.contrib import admin
from .models import LandingPageEntry

# Register your models here.

class LandingPageEntryAdmin(admin.ModelAdmin):
    list_display=("name","email","timestamp","updated")
    search_fields=["name", "email"]
    read_only_fields=["name","email","timestamp","updated"]

    list_filter=["active","timestamp"]


admin.site.register(LandingPageEntry,LandingPageEntryAdmin)
