# Generated by Django 2.1.2 on 2018-11-14 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventes', '0005_remove_produit_idcategorieproduit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vente',
            name='idMethodePaiement',
        ),
        migrations.DeleteModel(
            name='MethodePaiement',
        ),
    ]
