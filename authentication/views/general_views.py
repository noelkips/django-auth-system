from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User




def index(request):
    return render(request, "index.html")

def signup(request):
    return render(request, 'registration/signup_request.html')

def login_view(request):
    if request.method == 'POST':
        mobile = request.POST['mobile']
        pass1 = request.POST['pass1']
        
        user = authenticate(mobile=mobile, password=pass1)
        
        if user is not None:
            login(request, user)
            fname = user.first_name
            messages.success(request, "Logged In Sucessfully!!")
            if user.student:
                return render(request, "student/student_dashboard.html", {'mobile':fname})
            elif user.teacher:
                return render(request, "teacher/teacher_dashboard.html", {'mobile':fname})
            else:
                return HttpResponseRedirect('admin/')
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('login')
    
    return render(request, "login.html")