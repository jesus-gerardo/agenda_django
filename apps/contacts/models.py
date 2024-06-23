from django.db import models

# Create your models here.
class Contact(models.Model):
    
    name = models.CharField(max_length=128, verbose_name='nombres')
    first_name = models.CharField(max_length=128, verbose_name='primer apellido')
    last_name = models.CharField(max_length=128, verbose_name='segundo apellido', null=True)
    picture = models.ImageField(upload_to='contacts/', null=True)
    birthday = models.DateField(null=True)
    email = models.CharField(max_length=128, verbose_name="correo electronico", null=True)
    facebook = models.CharField(max_length=128, verbose_name="facebook", null=True)
    x = models.CharField(max_length=128, verbose_name="antiguo twitter", null=True)
    linkedin = models.CharField(max_length=128, verbose_name="linkedin", null=True)
    active = models.BooleanField(verbose_name='activo', default=True )

    class Meta:
        db_table="contact"

class ContactPhoneNumbers(models.Model):
    tel = models.CharField(max_length=20, verbose_name='telefono')
    contact = models.ForeignKey(Contact, on_delete=models.DO_NOTHING)

    class Meta:
        db_table='contact_phone_numbers'