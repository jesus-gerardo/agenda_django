from rest_framework.serializers import ModelSerializer
from .models import Reminder

class ReminderSerializer(ModelSerializer):
    class Meta:
        model = Reminder
        fields = '__all__'

class RemindersCreateSerializer(ModelSerializer):
    class Meta:
        model=Reminder
        fields= ['title', 'description', 'reminder_date', 'reminder_hour',]

    def create(self, validated_data):
        return Reminder.objects.create(active=True, **validated_data)
    
class RemindersUpdateSerializer(ModelSerializer):
    class Meta:
        model=Reminder
        fields= ['title', 'description', 'reminder_date', 'reminder_hour',]