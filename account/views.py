# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views import generic
from django.views.generic import CreateView, TemplateView
from account.models import Author
from django.http import HttpResponse
from django.template.response import TemplateResponse
from account.forms import RegisterUserForm, LoginUserForm, AuthorForm
# import stripe
# Create your views here.


class RegisterUserView(CreateView):
	form_class = RegisterUserForm
	template_name = "account/register.html"

	def dispatch(self, request, *args, **kwargs):
		# if request.user.is_authenticated():
			# return HttpResponseForbidden()
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

class DensityView(generic.CreateView):
	form_class = AuthorForm
	template_name = 'account/density.html'
	def density_Render(self, request):
		return render(request, 'account/density.html',{'KeyName': 'count_corb',})	

class IndexView(CreateView):
	form_class = RegisterUserForm # I am ONLY doing this to prevent an error when returning to homepage from login.html
	template_name = "index.html"
	def index_Render(self, request):
		return render(request, 'index.html')

#def contact(request):
#	return render(request,{'Values':'string1'})


def search(request):
	output = 'Hello'
	return render(request, 'account/density.html', {'output':output})

# Set your secret key: remember to change this to your live secret key in production
# See your keys here: https://dashboard.stripe.com/account/apikeys
# def basicCharge(request):
# 	stripe.api_key = "sk_test_Yly7TTfLd1EnS9XNwfR0Hgqd"

# 	# Token is created using Checkout or Elements!
# 	# Get the payment token ID submitted by the form:
# 	token = request.form['stripeToken'] # Using Flask

# 	# Charge the user's card:
# 	charge = stripe.Charge.create(
# 	amount=10,
# 	currency="ngn",
# 	description="Example charge",
# 	source=token,
# 	)

