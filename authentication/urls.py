from django.urls import path
from .views import general_views, user, staff

urlpatterns = [
    #genral 
    path('', general_views.index, name="index"),
    path('accounts/signup', general_views.signup, name="signup_request"),
    path('accounts/login', general_views.login_view, name="login"),

    path('accounts/signup/user/', user.user_signup, name='user_signup'),
    path('accounts/signup/staff/', staff.staff_signup, name='staff_signup'),

]