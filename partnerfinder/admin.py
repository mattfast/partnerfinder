from django.contrib import admin

from .models import *

admin.site.register(Instructor)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(TimeSlot)
admin.site.register(Availability)
admin.site.register(Enrollment)
admin.site.register(Instruction)
admin.site.register(PreviousCourse)
admin.site.register(Assignment)
admin.site.register(Posting)
