# Generated by Django 4.0.4 on 2022-05-21 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_alter_leave_list_qrcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='qr_code',
            field=models.ImageField(blank=True, upload_to='leave'),
        ),
    ]
