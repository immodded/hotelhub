from django.urls import path
from . import views
urlpatterns = [
    path("password_update/", views.PasswordUpdateView.as_view(), name='password-update'),
    path("profile/", views.ProfileView, name='profile'),
    path("Profile/update", views.ProfileUpdateView.as_view(), name = 'profile-update'),
]