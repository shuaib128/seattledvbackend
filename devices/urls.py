from django.urls import path
from .views import DevicesView, DeviceSearch

urlpatterns = [
    path('', DevicesView.as_view()),
    path('search', DeviceSearch.as_view()),
]