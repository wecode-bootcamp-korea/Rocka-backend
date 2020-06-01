# Generated by Django 3.0.6 on 2020-05-31 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20200530_1022'),
        ('product', '0002_auto_20200530_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='shipping_information',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.ShippingInformation'),
        ),
    ]