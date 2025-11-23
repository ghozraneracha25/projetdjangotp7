from django.urls import path
from .views import HelloView, StudentView

urlpatterns = [
    path('hello/', HelloView.as_view(), name='hello'),
    path('students/', StudentView.as_view(), name='students'),
]