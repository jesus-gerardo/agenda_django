from django.urls import path, include
from .reminders.views import RemindersViewSet
from rest_framework.routers import DefaultRouter

route = DefaultRouter()
route.register(r'reminders', RemindersViewSet, basename='reminders')

urlpatterns = [
    path('', include(route.urls))
]