# Generated by Django 3.1.3 on 2020-11-15 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retail_app1', '0009_auto_20201115_0605'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='image2',
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(default='static/media/index.png', upload_to='static/media'),
        ),
        migrations.AddField(
            model_name='product',
            name='image4',
            field=models.ImageField(default='static/media/index.png', upload_to='static/media'),
        ),
        migrations.AddField(
            model_name='product',
            name='main_image',
            field=models.ImageField(default='static/media/index.png', upload_to='static/media'),
        ),
    ]
