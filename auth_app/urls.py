from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.UserRegisterAPIViews.as_view(), name='registration')
]
