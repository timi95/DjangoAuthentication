from django.conf.urls import url
from django.views.generic.base import TemplateView
from account.views import RegisterUserView
from django.contrib.auth.views import logout
from Project2 import settings

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
	url(r'^register/$', view=RegisterUserView.as_view(), name='register'),
	url(r'^users/login/$', TemplateView.as_view(template_name='registration/login.html'), name='login2'),
	url(r'^login/$', TemplateView.as_view(template_name='home.html'), name='login'),
	url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
	url(r'^index/$', TemplateView.as_view(template_name='index.html'), name='index'),
]
