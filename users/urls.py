from django.urls import path

from . import views

from knox.views import LogoutView, LogoutAllView

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login),
    path('user/', views.user),
    path('logout/', LogoutView.as_view()),
    path('logout-all/', LogoutAllView.as_view()),
    path('google-authorize/', views.google_authorize),
    path('redirect/', views.redirect_google)
]