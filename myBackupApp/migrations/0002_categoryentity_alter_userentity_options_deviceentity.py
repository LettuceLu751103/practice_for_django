# Generated by Django 4.2.1 on 2023-05-14 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myBackupApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryEntity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': '類別管理',
                'verbose_name_plural': '類別管理',
                'db_table': 't_category',
            },
        ),
        migrations.AlterModelOptions(
            name='userentity',
            options={'verbose_name': '用戶管理', 'verbose_name_plural': '用戶管理'},
        ),
        migrations.CreateModel(
            name='DeviceEntity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField(verbose_name='價格')),
                ('vendor', models.CharField(max_length=30)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myBackupApp.categoryentity')),
            ],
            options={
                'verbose_name': '設備管理',
                'verbose_name_plural': '設備管理',
                'db_table': 't_device',
            },
        ),
    ]