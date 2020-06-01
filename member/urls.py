from django.urls import path
from .views import SignUpView, SignInView

urlpatterns = [
    path('/join', SignUpView.as_view()),
    path('/login', SignInView.as_view()),
]
