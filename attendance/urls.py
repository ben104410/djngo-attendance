from django.urls import path
from . import views

urlpatterns = [
    path('', views.attendance_dashboard, name='attendance_dashboard'),
    path('check-in/', views.mark_check_in, name='check_in'),
    path('check-out/', views.mark_check_out, name='check_out'),

    path('', views.attendance_dashboard, name='dashboard'),
]
