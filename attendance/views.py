from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import JsonResponse
from .models import Attendance
from datetime import date

@login_required
def attendance_dashboard(request):
    if request.user.is_superuser:
        records = Attendance.objects.all().order_by('-date')
    else:
        records = Attendance.objects.filter(user=request.user).order_by('-date')
    return render(request, 'attendance/dashboard.html', {'records': records})

@login_required
def mark_check_in(request):
    today = date.today()
    already_checked_in = Attendance.objects.filter(user=request.user, date=today).exists()
    if not already_checked_in:
        Attendance.objects.create(
            user=request.user,
            check_in=timezone.now().time(),
            status='present'
        )
    return redirect('attendance_dashboard')

@login_required
def mark_check_out(request):
    today = date.today()
    record = Attendance.objects.filter(user=request.user, date=today).first()
    if record and not record.check_out:
        record.check_out = timezone.now().time()
        record.save()
    return redirect('attendance_dashboard')

@login_required
def my_attendance_api(request):
    records = Attendance.objects.filter(user=request.user).values('date', 'check_in', 'check_out', 'status')
    return JsonResponse(list(records), safe=False)
