# Generated by Django 3.1.3 on 2020-11-14 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retail_app1', '0007_auto_20201113_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='picture',
            field=models.ImageField(default='/media/1.jfif', upload_to='', verbose_name='/media/'),
        ),
    ]