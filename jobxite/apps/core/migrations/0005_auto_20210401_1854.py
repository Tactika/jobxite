# Generated by Django 3.1.7 on 2021-04-02 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210329_1817'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='long_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='image_main',
            field=models.ImageField(blank=True, null=True, upload_to='static'),
        ),
    ]