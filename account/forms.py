from django import forms
from django.contrib.auth.models import User
from .models import Author


class RegisterUserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	password2 = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username','email']

		
	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password2'] != cd['password']:
			raise forms.ValidationError("Passwords don't match")
		return cd['password2']

class LoginUserForm(forms.ModelForm):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username','password']

	def validLogin(self):
		return True

class AuthorForm(forms.ModelForm):
	name = forms.CharField()
	class Meta:
		model = Author
		fields = [
			'name',
			'created_by'
		]