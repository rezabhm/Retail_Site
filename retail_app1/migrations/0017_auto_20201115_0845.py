# Generated by Django 3.1.3 on 2020-11-15 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('retail_app1', '0016_order_user_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user_key',
            field=models.ForeignKey(default='c', on_delete=django.db.models.deletion.CASCADE, to='retail_app1.user'),
        ),
    ]
