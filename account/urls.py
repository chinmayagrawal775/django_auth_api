from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('changepassword/', views.UserChangePasswordView.as_view(), name='changepassword'),
    path('sendpasswordresetlink/', views.SendPasswordChangeEmailView.as_view(), name='sendpasswordresetlink'),
    path('passwordreset/<uid>/<token>/', views.UserPasswordResetView.as_view(), name='passwordreset'),
]