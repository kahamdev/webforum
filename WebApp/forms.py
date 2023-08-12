from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import PhpCreateProfile,JavascriptCreateProfile,MeetPhpExpert,MeetJavascriptExpert


# php profile modelform
class PhpProfile(forms.ModelForm):
	class Meta:
		model=PhpCreateProfile
		fields='__all__'

# javascript profile modelform
class JavascriptProfile(forms.ModelForm):
	class Meta:
		model=JavascriptCreateProfile
		fields='__all__'


# meet php model form
class MeetPhp(forms.ModelForm):
	class Meta:
		model=MeetPhpExpert
		fields='__all__'


# meet javascript model form
class MeetJavascript(forms.ModelForm):
	class Meta:
		model=MeetJavascriptExpert
		fields='__all__'


# registration model form
# for later use
class RegistrationForm(UserCreationForm):
	 # email=forms.EmailField()
   
   class Meta:
         model=User
         fields=['username','email','password1','password2']








