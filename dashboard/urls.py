from django.urls import path
from . import views

urlpatterns = [
    
    #home
    path('', views.home, name='home'),
    
    #register user
    path('accounts/register/', views.RegisterView.as_view(), name='register'),
    
    #student enroll
    path('course/<int:course_id>/enroll/', views.enroll_course, name='enroll_course'),

    #admin crud
    path('course/create/', views.create_course, name='create_course'),
    path('course/<int:course_id>/edit/', views.edit_course, name='edit_course'),
    path('course/<int:course_id>/delete/', views.delete_course, name='delete_course'),
    
   
]