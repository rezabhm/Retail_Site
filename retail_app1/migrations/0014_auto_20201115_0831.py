# Generated by Django 3.1.3 on 2020-11-15 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('retail_app1', '0013_auto_20201115_0826'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='user_key',
        ),
    ]
