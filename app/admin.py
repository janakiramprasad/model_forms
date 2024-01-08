from django.contrib import admin

from app.models import *

# Register your models here.

class custamizeWebpage(admin.ModelAdmin):
    list_display=['topic_name','name','url','email']
    list_display_links=['url','name']
    list_editable=['email']
    search_fields=['name']
    list_filter=['name']

admin.site.register(Topic)

admin.site.register(Webpage,custamizeWebpage)

admin.site.register(AccessRecord)