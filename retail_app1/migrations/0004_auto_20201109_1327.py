# Generated by Django 3.1.3 on 2020-11-09 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retail_app1', '0003_auto_20201109_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='/image/index.png', upload_to='image'),
        ),
    ]
