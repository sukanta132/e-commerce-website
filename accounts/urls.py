# from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from .forms import MyChangePasswordForm
urlpatterns = [
    path('login/', views.LoginView.as_view(), name="LoginView"),
    path('logout', views.Logout_view, name="Logout_view"),
    path('registration', views.RegistrationView.as_view(), name="RegistrationView"),
    path('profile', views.ProfileView.as_view(), name="ProfileView"),
    # path('change-password', views.PasswordChangeView.as_view(),)
    # path('password', auth_views.PasswordChangeView.as_view(template_name='accounts/change-password.html')),
    path('change-password', PasswordChangeView.as_view(template_name="accounts/password-change.html", form_class=MyChangePasswordForm), name='change-password'),
    path('password-change-done', PasswordChangeDoneView.as_view(), name="password_change_done")

]