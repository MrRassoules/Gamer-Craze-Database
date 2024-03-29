# Generated by Django 2.2.2 on 2019-12-03 21:50

from django.db import migrations, models
import inventory.models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20191201_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=7, validators=[inventory.models.validate_positive]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=7, validators=[inventory.models.validate_positive]),
            preserve_default=False,
        ),
    ]
