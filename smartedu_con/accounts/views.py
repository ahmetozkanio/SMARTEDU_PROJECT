from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .forms import LoginForm, RegisterForm
from courses.models import Course
# Create your views here.


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username,
                                        password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')

                else:
                    messages.info(request, 'Disabled Account')

            else:
                messages.info(request, 'Check Your Username and Password')

    else:
        form = LoginForm()

    return render(request, 'login.html', {'form':form})


def user_register(request):
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account has been created, You can Login')
            return redirect('login')

    else:
        form = RegisterForm()        
    return render(request,'register.html',{'form':form})



def user_logout(request):
    logout(request)
    return redirect('index')

@login_required(login_url='login')
def user_dashboard(request):
    #hangi kullanici giris yapmissa
    current_user =request.user

    #Ogrencinin kayit oldugu kurslar
    #manytomanyt related name = courses_joined
    courses = current_user.courses_joined.all()
    context = {
        'courses':courses
    }
    return render(request,'dashboard.html',context)

#kurs ekleme
def enroll_the_course(request):
    course_id =  request.POST['course_id']#course.html
    user_id = request.POST['user_id']
    course = Course.objects.get(id= course_id)
    user = User.objects.get(id = user_id)
    #ilgili course a user eklenmis oldu
    course.students.add(user)
    return redirect('dashboard')

#kurs silme
def release_the_course(request):
    course = Course.objects.get(id= request.POST['course_id'])
    user = User.objects.get(id = request.POST['user_id'])
    #ilgili course a user eklenmis oldu
    course.students.remove(user)
    return redirect('dashboard')