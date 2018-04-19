from django.contrib import admin
from .models import *
from django.forms import widgets

admin.site.register(EventTime)
admin.site.register(Club)
admin.site.register(Member)
admin.site.register(Participant)
admin.site.register(Attendance)    

class EventAdmin( admin.ModelAdmin ):
    list_display=['title', 'description', 'created_timestamp', 'organizing_club', 'organizing_chairman', 'status', 'image', 'venue', 'additional_info']

    def save_model(self, request, obj, form, change):
        obj.title = "name here"
        obj.save() 

admin.site.register( Event, EventAdmin )

