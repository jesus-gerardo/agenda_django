from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Reminder(models.Model):
    title = models.CharField(max_length=128, verbose_name='titulo')
    description = models.CharField(max_length=512, verbose_name='descripcion', null=True)
    reminder_date = models.DateField(verbose_name='fecha_recordatorio')
    reminder_hour = models.TimeField(verbose_name='hora_recordatorio')
    active = models.BooleanField(verbose_name='active', default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    class Meta:
        db_table='reminders'