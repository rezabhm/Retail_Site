# Generated by Django 3.1.3 on 2020-11-09 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retail_app1', '0005_auto_20201109_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='media/retail_app1/index.png', upload_to='media/retail_app1'),
        ),
    ]
