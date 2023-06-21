from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django import forms
from django.contrib.auth.models import User
from user_profile.models import UserProfile

class UserAuthenticationForm(AuthenticationForm):
    """ extending django's authenticationform form to add form-control class """
    next_url = forms.CharField(widget=forms.HiddenInput(), required=False)
    def __init__(self, *args, **kwargs):
        super(UserAuthenticationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    # class Meta:
    #     widgets = {
    #         'username' : forms.TextInput(attrs = {
    #             'class' : 'form-control',
    #             'placeholder' : 'username...'
    #         }),
    #         'password' : forms.PasswordInput(attrs = {
    #             'class' : 'form-control',
    #             'placeholder' : 'password...',
    #         })
        
    #     }



class UserRegistrationForm(UserCreationForm):
    """ extending django's usercreation form to add form-control class """
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserProfileForm(forms.ModelForm):
    ''' form to update users basic information '''
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
     
       
class UserForm(forms.ModelForm):
    ''' form to update user's aditional information '''
    class Meta:
        model = UserProfile
        fields = ['mobile', 'address']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


# class PasswordChangingForm(PasswordChangeForm):
    ''' password reset form '''
    # old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    # new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    # new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    # class Meta:
    #     model = User
    #     fields = ['old_password', 'new_password1', 'new_password2']


#forms.py
# from django.contrib.auth.forms import PasswordChangeForm

# class ChangePasswordForm(PasswordChangeForm):
    
#     def _init_(self, args, *kwargs):
#         """ Add Class : form-control to every fields """
#         super()._init_(*args, **kwargs)
#         for field in iter(self.fields):
#             self.fields[field].widget.attrs.update({
#                 'class': 'form-control',
#                 'placeholder':  f'Enter {str(field.replace("_", " "))}',
#                 'required' : False
#             }) 


class MyChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="old password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True, 'class': 'form-control'}),
    )
    new_password1 = forms.CharField(
        label="New Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True, 'class': 'form-control'}),
    )
    new_password2 = forms.CharField(
        label="New Password Again",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True, 'class': 'form-control'}),
    )