from django import forms
from django.contrib.auth.models import User
from .models import CommentModel



class UserRegistrationForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['username','password','email']
    widgets = {
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}), 
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Email'}),
    }
    
class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}))
    options=(('writer','writer'),('viewer','viewer'))
    usertype = forms.ChoiceField(choices=options,widget=forms.Select(attrs={'class':'form-control'}))
    
class AddCommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['description']
        widgets={
            "description":forms.TextInput(attrs={'class':'form-control','placeholder':'comment here...'})
        }
    