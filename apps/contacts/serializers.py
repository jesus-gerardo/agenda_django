
from rest_framework import serializers
from .models import Contact,ContactPhoneNumbers
import ast

class ContacPhoneNumberstSerializer(serializers.ModelSerializer):
    # Nested relationships drf

    class Meta:
        model=ContactPhoneNumbers
        fields = ['tel']

class ContactSerializer(serializers.ModelSerializer):
    phone = ContacPhoneNumberstSerializer(many=True)

    class Meta:
        model=Contact
        fields = '__all__'
        read_only_fields = ['id']

class ContactCreateSerializer(serializers.ModelSerializer):
    picture = serializers.ImageField(use_url=True, required=False)
    phones = serializers.CharField(required=False, help_text="[number,...]")
    # phones = serializers.ListField(
    #     child =serializers.CharField(),
    #     required=False
    # )
        
    class Meta:
        model=Contact
        fields=['name', 'first_name', 'last_name', 'picture', 'birthday', 'email', 'facebook', 'x', 'linkedin', 'phones']

    def create(self, validated_data):
        phone = validated_data.pop('phones')
        contact = Contact.objects.create(active=True, **validated_data)
        
        for numbers in ast.literal_eval(phone):
            ContactPhoneNumbers.objects.create(contact=contact, tel=numbers)

        return contact
    
class ContactUpdateSerializer(serializers.ModelSerializer):
    phones = serializers.CharField(required=False, help_text="[number,...]")
    
    class Meta:
        model=Contact
        fields=['name', 'first_name', 'last_name', 'birthday', 'email', 'facebook', 'x', 'linkedin', 'phones']
        read_only_fields = ['id']

    def update(self, instance, validated_data):
        phone = validated_data.pop('phones')

        instance.name = validated_data.get('name', instance.name)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.birthday = validated_data.get('birthday', instance.birthday)
        instance.email = validated_data.get('email', instance.email)
        instance.facebook = validated_data.get('facebook', instance.facebook)
        instance.x = validated_data.get('x', instance.x)
        instance.linkedin = validated_data.get('linkedin', instance.linkedin)
        instance.save()

        ContactPhoneNumbers.objects.filter(contact=instance.id).delete()
        for numbers in ast.literal_eval(phone):
            ContactPhoneNumbers.objects.create(contact=instance, tel=numbers)
        return instance