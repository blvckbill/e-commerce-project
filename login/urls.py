from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='loginPage'),
    path('signup/', views.create_user, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('resetpassword/', views.password_reset, name='forgotPassword'),
]