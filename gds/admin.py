from django.contrib import admin

from . models import *

admin.site.register(SchedChange)
admin.site.register(Passenger)
admin.site.register(Reservation)
admin.site.register(Travel)
admin.site.register(SegmentSched)