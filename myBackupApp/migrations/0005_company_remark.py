# Generated by Django 4.2.1 on 2023-05-16 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBackupApp', '0004_company_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='remark',
            field=models.TextField(blank=True, null=True),
        ),
    ]