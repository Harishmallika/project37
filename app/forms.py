from django import forms

from app.models import *

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email']
        widgets={'password':forms.PasswordInput}
        help_text={'username':''}

class profileForm(forms.ModelForm):
    class Meta:
        model=profile
        fields=['address','profile_pic']        