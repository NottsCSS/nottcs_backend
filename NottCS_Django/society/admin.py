from django.contrib import admin
from .models import *

admin.site.register(Event)
admin.site.register(EventTime)
admin.site.register(Club)
admin.site.register(Member)
admin.site.register(Participant)
admin.site.register(Attendance)