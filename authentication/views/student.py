from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from ..models import Student



def student_signup(request):
    if request.method == 'POST':
        mobile = request.POST['mobile']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password= request.POST['password']
        password2= request.POST['password-confirm']
        email = request.POST['email']
        if password != password2:
            messages.error(request, "Password doesn't match ! check your password and try again")
            return redirect('student_signup')
        user = Student.objects.create_user(first_name = first_name, last_name = last_name, 
        password = password , email = email, mobile=mobile)
        # user.user_type = 1
        user.save()
        return redirect('login')
    return render(request, 'registration/user_signup.html')