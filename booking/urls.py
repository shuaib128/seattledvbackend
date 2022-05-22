from django.urls import path
from .views import ServicesView, UserView, BookingView

urlpatterns = [
    path('', ServicesView.as_view()),
    path('user', UserView.as_view()),
    path('book', BookingView.as_view()),
]