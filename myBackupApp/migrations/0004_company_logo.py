# Generated by Django 4.2.1 on 2023-05-16 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBackupApp', '0003_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='company'),
        ),
    ]
