# Generated by Django 2.2.2 on 2019-12-01 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mtgcard',
            name='card_subtype',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mtgcard',
            name='rule_text',
            field=models.TextField(blank=True, max_length=400),
        ),
    ]