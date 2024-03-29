# Generated by Django 2.2.2 on 2019-12-01 23:33

from django.db import migrations, models
import django.db.models.deletion
import inventory.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MTGCard',
            fields=[
                ('SKU_ID', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('card_name', models.CharField(max_length=30)),
                ('number', models.PositiveIntegerField()),
                ('rarity', models.CharField(choices=[('B', 'Basic'), ('C', 'Common'), ('U', 'Uncommon'), ('R', 'Rare'), ('M', 'Mythic Rare')], max_length=1)),
                ('color', models.CharField(choices=[('W', 'White'), ('U', 'Blue'), ('B', 'Black'), ('R', 'Red'), ('G', 'Green')], max_length=1)),
                ('card_type', models.CharField(choices=[('Artifact', 'Artifact'), ('Creature', 'Creature'), ('Enchantment', 'Enchantment'), ('Instant', 'Instant'), ('Land', 'Land'), ('Legendary', 'Legendary'), ('Planeswalker', 'Planeswalker'), ('Sorcery', 'Sorcery')], max_length=12)),
                ('card_subtype', models.CharField(blank=True, max_length=20)),
                ('converted_cost', models.PositiveIntegerField()),
                ('rule_text', models.TextField(blank=True, max_length=400)),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'ordering': ['card_name'],
            },
        ),
        migrations.CreateModel(
            name='MTGSet',
            fields=[
                ('expansion_code', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('set_name', models.CharField(max_length=20)),
                ('set_size', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MTGSingle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.CharField(choices=[('NM', 'Near Mint'), ('LP', 'Lightly Played'), ('MP', 'Moderately Played'), ('HP', 'Heavily Played'), ('DM', 'Damaged')], max_length=2)),
                ('language', models.CharField(choices=[('EN', 'English'), ('SP', 'Spanish'), ('FR', 'French'), ('DE', 'German'), ('IT', 'Italian'), ('PT', 'Portuguese'), ('JP', 'Japanese'), ('KR', 'Korean'), ('RU', 'Russian'), ('CS', 'Simplified Chinese'), ('CT', 'Traditional Chinese')], max_length=2)),
                ('qty', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, validators=[inventory.models.validate_positive])),
                ('SKU_ID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.MTGCard')),
            ],
            options={
                'ordering': ['language', 'condition'],
                'unique_together': {('SKU_ID', 'condition', 'language')},
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('customer_id', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveIntegerField(default=0)),
                ('order_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.Order')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.MTGSingle')),
            ],
        ),
        migrations.AddField(
            model_name='mtgcard',
            name='set',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.MTGSet'),
        ),
    ]
