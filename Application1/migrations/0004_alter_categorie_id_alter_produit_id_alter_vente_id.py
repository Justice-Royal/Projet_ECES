# Generated by Django 4.2.2 on 2023-07-01 22:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Application1", "0003_rename_quantité_reçu_produit_quantite_emise_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="categorie",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="produit",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="vente",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
