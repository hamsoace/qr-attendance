# Generated by Django 4.0.4 on 2022-05-19 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Attendance',
        ),
        migrations.DeleteModel(
            name='Attendance_List',
        ),
        migrations.DeleteModel(
            name='Leave',
        ),
        migrations.DeleteModel(
            name='Leave_List',
        ),
    ]
