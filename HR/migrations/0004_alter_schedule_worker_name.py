# Generated by Django 4.0.2 on 2022-02-14 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_permission'),
        ('HR', '0003_alter_schedule_worker_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='worker_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.workers'),
        ),
    ]
