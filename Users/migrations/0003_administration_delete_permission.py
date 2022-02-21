# Generated by Django 4.0.2 on 2022-02-15 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_permission'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('password', models.CharField(max_length=254)),
                ('phone_number', models.CharField(max_length=254)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='Permission',
        ),
    ]
