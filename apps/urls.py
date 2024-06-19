from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .reminders.views import RemindersViewSet
from .contacts.views import ContactViewSet

route = DefaultRouter()
route.register(r'reminders', RemindersViewSet, basename='reminders')
route.register(r'contacts', ContactViewSet, basename='contacts')

urlpatterns = [
    path('', include(route.urls))
]