# Generated by Django 5.1.6 on 2025-05-14 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prodotti', '0004_prodotto_preferiti'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Preferito',
        ),
    ]
