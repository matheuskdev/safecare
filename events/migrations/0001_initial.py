# Generated by Django 5.1.1 on 2024-11-13 12:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("departments", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Gender",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField(help_text="Gênero", max_length=255)),
            ],
            options={
                "verbose_name": "Gênero",
                "verbose_name_plural": "Gêneros",
                "ordering": ["name"],
                "indexes": [
                    models.Index(
                        fields=["name"], name="events_gend_name_3a83e2_idx"
                    )
                ],
            },
        ),
        migrations.CreateModel(
            name="Race",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField(help_text="Raça", max_length=255)),
            ],
            options={
                "verbose_name": "Raça",
                "verbose_name_plural": "Raças",
                "ordering": ["name"],
                "indexes": [
                    models.Index(
                        fields=["name"], name="events_race_name_fadc17_idx"
                    )
                ],
            },
        ),
        migrations.CreateModel(
            name="EventPatient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_deleted", models.BooleanField(default=False)),
                (
                    "patient_name",
                    models.CharField(
                        help_text="Nome do paciente", max_length=225
                    ),
                ),
                (
                    "attendance",
                    models.IntegerField(help_text="Número do Atendimento"),
                ),
                (
                    "record",
                    models.IntegerField(help_text="Número do prontuário."),
                ),
                (
                    "birth_date",
                    models.DateField(help_text="Data de nascimento."),
                ),
                (
                    "internment_date",
                    models.DateField(help_text="Data de internação."),
                ),
                (
                    "genere",
                    models.ForeignKey(
                        blank=True,
                        help_text="Gênero",
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="event_genere",
                        to="events.gender",
                    ),
                ),
                (
                    "race",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="event_race",
                        to="events.race",
                    ),
                ),
            ],
            options={
                "verbose_name": "Paciente Ocorrência",
                "verbose_name_plural": "Pacientes Ocorrências",
                "ordering": ["created_at"],
            },
        ),
        migrations.CreateModel(
            name="EventOcurrence",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_deleted", models.BooleanField(default=False)),
                (
                    "patient_involved",
                    models.BooleanField(
                        default=False,
                        help_text="A ocorrência envolveu algum paciente ?",
                    ),
                ),
                (
                    "ocurrence_date",
                    models.DateField(help_text="Data da ocorrência"),
                ),
                (
                    "ocurrence_time",
                    models.TimeField(help_text="Hora da ocorrência"),
                ),
                (
                    "description_ocurrence",
                    models.TextField(help_text="Descrição da ocorrência"),
                ),
                (
                    "immediate_action",
                    models.TextField(
                        help_text="O que foi realizado após a ocorrência / Ação imediata"
                    ),
                ),
                (
                    "notified_department",
                    models.ForeignKey(
                        help_text="Setor que está sendo notificado",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="notified_events",
                        to="departments.department",
                    ),
                ),
                (
                    "reporting_department",
                    models.ForeignKey(
                        help_text="Setor que está reportando",
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="reporting_events",
                        to="departments.department",
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        blank=True,
                        help_text="Paciente envolvido na ocorrência",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="patient_events",
                        to="events.eventpatient",
                    ),
                ),
            ],
            options={
                "verbose_name": "Ocorrência",
                "verbose_name_plural": "Ocorrências",
                "ordering": ["created_at"],
                "indexes": [
                    models.Index(
                        fields=["patient_involved"],
                        name="events_even_patient_b6b9d1_idx",
                    ),
                    models.Index(
                        fields=["ocurrence_date"],
                        name="events_even_ocurren_6fa75d_idx",
                    ),
                    models.Index(
                        fields=["reporting_department"],
                        name="events_even_reporti_66644f_idx",
                    ),
                    models.Index(
                        fields=["notified_department"],
                        name="events_even_notifie_1b9ac4_idx",
                    ),
                ],
            },
        ),
        migrations.AddIndex(
            model_name="eventpatient",
            index=models.Index(
                fields=["patient_name"], name="events_even_patient_54b3e6_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="eventpatient",
            index=models.Index(
                fields=["attendance"], name="events_even_attenda_7c30a0_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="eventpatient",
            index=models.Index(
                fields=["record"], name="events_even_record_390175_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="eventpatient",
            index=models.Index(
                fields=["birth_date"], name="events_even_birth_d_25fbef_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="eventpatient",
            index=models.Index(
                fields=["internment_date"],
                name="events_even_internm_28716c_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="eventpatient",
            index=models.Index(
                fields=["genere"], name="events_even_genere__eb75c9_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="eventpatient",
            index=models.Index(
                fields=["race"], name="events_even_race_id_b10d79_idx"
            ),
        ),
    ]
