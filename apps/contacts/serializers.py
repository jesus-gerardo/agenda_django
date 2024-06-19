
from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields = '__all__'

class ContactCreateSerializer(serializers.ModelSerializer):
    picture = serializers.ImageField(use_url=True, required=False)
        
    class Meta:
        model=Contact
        fields=['name', 'first_name', 'last_name', 'picture', 'birthday', 'email', 'facebook', 'x', 'linkedin',]

    def create(self, validated_data):
        return Contact.objects.create(active=True, **validated_data)
    
class ContactUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields=['name', 'first_name', 'last_name', 'picture', 'birthday', 'email', 'facebook', 'x', 'linkedin',]

    # def update(self, instance, validated_data):
    #     return super().update(instance, validated_data)