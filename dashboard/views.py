from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import Course, Enrollment
from django.contrib.auth import get_user_model 
from .forms import CourseForm, CustomUserCreationForm
# from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Course, Enrollment
from django.urls import reverse_lazy
from django.views import generic



#====================================Student Section=================================================

def home(request):
    courses = Course.objects.all()
    return render(request, 'dashboard/home.html', {'courses': courses})

#registration
class RegisterView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'



#enrollment
@login_required
def enroll_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    enrollment, created = Enrollment.objects.get_or_create(student=request.user, course=course)
    
    if created:
        messages.success(request, f"Successfully enrolled in {course.title}")
    else:
        messages.info(request, f"You are already enrolled in {course.title}")
    
    return redirect('home')




#==========================================Admin Section=============================================


def is_admin(user):
    return user.is_staff or user.is_superuser

#Create course
@user_passes_test(is_admin)
def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Course created successfully!")
            return redirect('home')
    else:
        form = CourseForm()
    
    return render(request, 'dashboard/course_form.html', {'form': form})


#edit course
@user_passes_test(is_admin)
def edit_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully!")
            return redirect('home')
    else:
        form = CourseForm(instance=course)
    
    return render(request, 'dashboard/course_form.html', {'form': form, 'course': course})


#delete course
@user_passes_test(is_admin)
def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    
    if request.method == 'POST':
        course.delete()
        messages.success(request, "Course deleted successfully!")
        return redirect('home')
    
    return render(request, 'dashboard/course_confirm_delete.html', {'course': course})

    

