# Generated by Django 3.0.2 on 2020-01-12 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineShop', '0003_auto_20200111_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/images/'),
        ),
    ]