from django.conf.urls import url
from django.views.generic.base import TemplateView
from account.views import RegisterUserView, LoginUserView, IndexView, DensityView
from django.contrib.auth.views import logout
from . import views
from Project2 import settings

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
	 url(r'^index/$', IndexView.as_view(), name='index'),
	 url(r'^register/$', RegisterUserView.as_view(), name='register'),
	 url(r'^login/$', view=LoginUserView.as_view(), name='login'),
	 url(r'^logout/$', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
	 url(r'^contact/$',TemplateView.as_view(template_name='account/contact.html'), name='contact'),
	 url(r'^density/$',DensityView.as_view(template_name='account/density.html'), name='density'),
	 url(r'^search$', views.search,name='search'),
]
