# Generated by Django 2.2.10 on 2020-02-10 02:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Resource",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("label", models.CharField(max_length=100, verbose_name="Libellé")),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("MEET", "Salle de réunion"),
                            ("CONF", "Salle de conférence"),
                            ("WORK", "Atelier"),
                            ("PROJ", "Projecteur vidéo"),
                            ("MISC", "Divers"),
                        ],
                        max_length=4,
                        verbose_name="Type de ressource",
                    ),
                ),
                (
                    "location",
                    models.CharField(max_length=200, verbose_name="Emplacement"),
                ),
                (
                    "capacity",
                    models.IntegerField(default=0, verbose_name="Capacité d'accueil"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100, verbose_name="Objet")),
                ("start_date", models.DateTimeField(verbose_name="Début")),
                ("end_date", models.DateTimeField(verbose_name="Fin")),
                (
                    "resource",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="booking.Resource",
                    ),
                ),
            ],
        ),
    ]
