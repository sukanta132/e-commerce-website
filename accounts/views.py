from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from .forms import (
    UserAuthenticationForm,
    UserRegistrationForm,
    UserProfileForm,
    UserForm,
    )
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm


class LoginView(View):

    def get(self, request):       
        next_url = request.GET.get('next')
        # print(next_url)
        form = UserAuthenticationForm(initial={
            'next_url' : next_url
        })
        context = {
            'form' : form,
        }
        return render (request, 'accounts/login.html', context)
    

    def post(self, request):
        print(request.POST)
        form = UserAuthenticationForm(data=request.POST)
        if form.is_valid():
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password')
            # print(username, password)
            login(request, form.get_user())
            next_url = form.cleaned_data.get('next_url')
            if next_url:
                return redirect(next_url)
            print("login successful")
            print(request.user.is_authenticated)
            return redirect('home_page')
        else:
            print("invalid userename and password")
        context = {
            'form' : form,
        }
        return render (request, 'accounts/login.html', context)
    

class RegistrationView(View):
    form_class = UserRegistrationForm
    template_name = 'accounts/registration.html'

    def get(self, request):
        form = self.form_class()
        context = {
            'form' : form
        }
        return render (request, self.template_name, context)
    
    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('LoginView')
        else:
            print("invalid userename and password")
        context = {
            'form' : form,
        }
        return render(request, self.template_name, context)

@login_required
def Logout_view(request):
    logout(request)
    return redirect('home_page')

@method_decorator(login_required, name="dispatch")
class ProfileView(View):
    ''' user profile view '''
    profile_form_class = UserForm
    form_class = UserProfileForm
    template_name = 'accounts/profile.html'

    def get(self, request):
        if request.user.is_authenticated:
            user = User.objects.get(id=request.user.id)
            user_form = self.form_class(instance=user)
            print(user.user_profile)
            user_profile_form = self.profile_form_class(instance=user.user_profile)
            context = {
                'user_form' : user_form,
                'user_profile_form' : user_profile_form
            }
            print(user_profile_form)
            return render(request, self.template_name, context)
        return redirect('LoginView')
    

    def post(self, request):
        user = User.objects.get(id=request.user.id)
        # form = self.form_class(instance=user, data=request.POST) # for creation
        user_form = self.form_class(request.POST, instance=user) # for update
        user_profile_form = self.profile_form_class(request.POST, instance=user.user_profile)
        # x = request.POST.get('first_name')
        # y = request.POST.get('last_name')
        # print(x, y)        
        if user_form.is_valid() and user_profile_form.is_valid():
            user_form.save()
            user_profile_form.save()
            # first_name = form.cleaned_data.get('first_name')
            # last_name = form.cleaned_data.get('last_name')
            # print(first_name, last_name)
        context = {
            'user_form' : user_form,
            'user_profile_form' : user_profile_form
        }

        return render(request, self.template_name, context)




# @method_decorator(login_required, name="dispatch")
# class ChangePasswordView(View):
#     ''' user profile view '''
#     form_class = ChangePasswordForm
#     template_name = 'accounts/change-password.html'

#     def get(self, request):
#         if request.user.is_authenticated:
#             user = User.objects.get(id=request.user.id)
#             user_form = self.form_class(instance=user)
#             print(user.user_profile)
#             context = {
#                 'change_password' : user_form,
#             }
#             return render(request, self.template_name, context)
#         return redirect('LoginView')
    

#     def post(self, request):
#         user = User.objects.get(id=request.user.id)
#         user_form = self.form_class(request.POST, instance=user) # for update       
#         if user_form.is_valid():
#             user_form.save()
#             return redirect('LoginView')
#         context = {
#             'change_password' : user_form,
#         }

#         return render(request, self.template_name, context)