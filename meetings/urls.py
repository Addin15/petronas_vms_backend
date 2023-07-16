from django.urls import path
from . import views

urlpatterns = [
    path('meetings/', views.MeetingView.as_view()),
    path('invitations/<str:id>/', views.InvitationView.as_view()),
    path('invitations/<str:id>/qr/', views.generate_qr),
]
