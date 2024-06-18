from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import Reminder
from .serializers import ReminderSerializer, RemindersCreateSerializer, RemindersUpdateSerializer
from utils.pagination.CustomPagination import CustomPagination


# Create your views here.
class RemindersViewSet(ModelViewSet):
    queryset = Reminder.objects.filter(active=True)
    http_method_names=['get', 'post', 'put', 'delete']
    pagination_class = CustomPagination

    serializer_class = {
        'list': ReminderSerializer,
        'retrieve': ReminderSerializer,
        'create': RemindersCreateSerializer,
        'update': RemindersUpdateSerializer
    }

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ReminderSerializer
        if self.action in ['create']:
            return RemindersCreateSerializer
        if self.action in ['update']:
            return RemindersUpdateSerializer
        
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)