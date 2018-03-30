from django.contrib import admin
from .models import *
from django import forms
from django.forms import widgets

admin.site.register(EventTime)
admin.site.register(Club)
admin.site.register(Member)
admin.site.register(Participant)
admin.site.register(Attendance)

class EventAdminForm( forms.ModelForm ):    
    title = forms.CharField( max_length = 255, required = True )
    

class EventAdmin( admin.ModelAdmin ):
    fields  = ['title']
    form    = EventAdminForm
    
    def save_model(self, request, obj, form, change):
        obj.title = "name here"
        obj.save() 

admin.site.register( Event, EventAdmin )

