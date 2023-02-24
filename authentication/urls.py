from django.urls import path
from .views import general_views, student, teacher

urlpatterns = [
    #genral 
    path('', general_views.index, name="index"),
    path('signup', general_views.signup, name="signup_request"),
    path('login', general_views.login_view, name="login"),

    path('accounts/signup/student/', student.student_signup, name='student_signup'),
    path('accounts/signup/teacher/', teacher.teacher_signup, name='teacher_signup'),

]