# Generated by Django 5.0.6 on 2024-06-19 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_alter_contact_facebook_alter_contact_linkedin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='picture',
            field=models.ImageField(null=True, upload_to='contacts/'),
        ),
    ]
