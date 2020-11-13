from django.urls import path

from . import views

app_name = 'messenger'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('leave_message/', views.leave_message, name = 'leave_message'),
]