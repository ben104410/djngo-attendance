from django.contrib import admin
from .models import Attendance  # Make sure this import matches your model

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'check_in', 'check_out', 'status')
    list_filter = ('status', 'date')
    search_fields = ('user__username',)
