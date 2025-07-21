from django.db import models
from django.conf import settings  # For AUTH_USER_MODEL
from django.utils import timezone  # ✅ Correct import

class Attendance(models.Model):
    STATUS_CHOICES = [
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('late', 'Late'),
        ('excused', 'Excused'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=timezone.now)

    date = models.DateField(auto_now_add=True)
    check_in = models.TimeField(null=True, blank=True)
    check_out = models.TimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='present')
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user} - {self.timestamp}"
