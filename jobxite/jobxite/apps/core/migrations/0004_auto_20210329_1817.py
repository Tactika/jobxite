# Generated by Django 3.1.7 on 2021-03-30 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_item_image_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image_main',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]