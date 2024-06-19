from rest_framework import response, status
from rest_framework.viewsets import ModelViewSet
from .models import Contact, ContactPhoneNumbers
from utils.pagination.CustomPagination import CustomPagination
from .serializers import ContactSerializer, ContactCreateSerializer, ContactUpdateSerializer
from rest_framework.parsers import MultiPartParser

# Create your views here.
class ContactViewSet(ModelViewSet):
    queryset=Contact.objects.filter(active=True)
    pagination_class = CustomPagination
    http_method_names = ['get', 'post', 'put']
    parser_classes =[MultiPartParser]

    serializer_class = {
        'list': ContactSerializer,
        'retrieve': ContactSerializer,
        'create': ContactCreateSerializer,
        'update': ContactUpdateSerializer
    }

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ContactSerializer
        if self.action in ['create']:
            return ContactCreateSerializer
        if self.action in ['update']:
            return ContactUpdateSerializer
        
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.active = False
        instance.save()
        return response.Response(status=status.HTTP_204_NO_CONTENT)
        

