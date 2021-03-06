# Generated by Django 3.0.2 on 2020-02-11 10:31

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion
import onlineShop.fields


class Migration(migrations.Migration):

    dependencies = [
        ('onlineShop', '0006_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0, verbose_name='Quantity')),
                ('unit_price', onlineShop.fields.MoneyField(blank=True, decimal_places=127, default=Decimal('0'), max_digits=127, null=True, verbose_name='Unit price')),
                ('total_price', onlineShop.fields.MoneyField(blank=True, decimal_places=127, default=Decimal('0'), max_digits=127, null=True, verbose_name='Total price')),
                ('url', models.CharField(max_length=2000)),
                ('image', models.CharField(max_length=200, null=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='onlineShop.Cart')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
