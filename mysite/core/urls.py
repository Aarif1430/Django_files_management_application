from django.urls import path
from . import views


urlpatterns = [
	path('signup/', views.SignUp.as_view(), name='signup'),
	path('reset_password/', views.ResetPassword.as_view(), name='reset'),
]
