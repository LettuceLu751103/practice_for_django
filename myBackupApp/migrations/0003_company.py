# Generated by Django 4.2.1 on 2023-05-16 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myBackupApp', '0002_categoryentity_alter_userentity_options_deviceentity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('owner', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '公司管理',
                'verbose_name_plural': '公司管理',
                'db_table': 'tt_company',
            },
        ),
    ]
