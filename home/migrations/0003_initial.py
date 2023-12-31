# Generated by Django 4.0.4 on 2022-05-19 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0002_delete_attendance_delete_attendance_list_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('date', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('qr_code', models.ImageField(blank=True, upload_to='Attendance')),
            ],
            options={
                'verbose_name_plural': 'Attendance QR',
            },
        ),
    ]
