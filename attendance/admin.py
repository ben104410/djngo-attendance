from django.contrib import admin
from .models import Attendance  # Make sure this import matches your model

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'timestamp', 'status')  # Customize fields shown
    list_filter = ('status', 'timestamp')
    search_fields = ('user__username',)
