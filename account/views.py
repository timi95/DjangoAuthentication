# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import CreateView
from django.http import *
from account.forms import RegisterUserForm, LoginUserForm

# Create your views here.


class RegisterUserView(CreateView):
	form_class = RegisterUserForm
	template_name = "account/register.html"

	def dispatch(self, request, *args, **kwargs):
		if request.user.is_authenticated():
			return HttpResponseForbidden()


		return super(RegisterUserView, self).dispatch(request, *args, **kwargs)

	def form_valid(self, form):
		user = form.save(commit=False)
		user.set_password(form.cleaned_data['password'])
		user.save()
		return HttpResponse('User registered')

class LoginUserView(CreateView):
	form_class = LoginUserForm
	template_name = "account/login.html"
	def login_Render(self, request):
		return render(request, 'account/login.html')


class IndexView(CreateView):
	template_name = "account/index.html"
	def index_Render(self,request):
		return render(request, 'account/index.html')
