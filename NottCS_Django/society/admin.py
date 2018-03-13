from django.contrib import admin
from .models import *
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    fields = ('title', 'description','created_timestamp','organizing_chairman','status','fees','event_venue')
    list_display = ('title', 'description','created_timestamp','organizing_chairman','status','fees','event_venue')
    list_filter = ()

class MemberAdmin(admin.ModelAdmin):
    fields = ('queue_group', 'queue_station', 'queue_start_time', 'queue_end_time',)
    list_filter = (('queue_station', admin.RelatedOnlyFieldListFilter),('queue_group', admin.RelatedOnlyFieldListFilter))

admin.site.register(Event,EventAdmin)
admin.site.register(Club)
admin.site.register(Member)