from rest_framework import serializers
from .models import Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # Shows username instead of ID

    class Meta:
        model = Attendance
        fields = ['id', 'user', 'date', 'check_in', 'check_out', 'status', 'remarks']
