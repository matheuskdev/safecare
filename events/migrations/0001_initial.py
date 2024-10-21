# Generated by Django 5.1.1 on 2024-10-21 16:36

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classifications', '0001_initial'),
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventPatient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('patient_name', models.CharField(help_text='Nome do paciente', max_length=225)),
                ('attendance', models.IntegerField(help_text='Número do Atendimento', validators=[django.core.validators.MinLengthValidator(9999, 'O número do atendimento deve conter no mínimo 5 caracteres')])),
                ('record', models.IntegerField(help_text='Número do prontuário.', validators=[django.core.validators.MinLengthValidator(1, 'O valor mínimo do prontuário é 1.')])),
                ('birth_date', models.DateField(help_text='Data de nascimento.')),
                ('internment_date', models.DateField(help_text='Data de internação.')),
            ],
            options={
                'verbose_name': 'Paciente Ocorrência',
                'verbose_name_plural': 'Pacientes Ocorrências',
                'ordering': ['created_at'],
                'indexes': [models.Index(fields=['patient_name'], name='events_even_patient_54b3e6_idx'), models.Index(fields=['attendance'], name='events_even_attenda_7c30a0_idx'), models.Index(fields=['record'], name='events_even_record_390175_idx'), models.Index(fields=['birth_date'], name='events_even_birth_d_25fbef_idx'), models.Index(fields=['internment_date'], name='events_even_internm_28716c_idx')],
            },
        ),
        migrations.CreateModel(
            name='EventOcurrence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('patient_involved', models.BooleanField(default=False, help_text='A ocorrência envolveu algum paciente ?')),
                ('ocurrence_date', models.DateField(help_text='Data da ocorrência')),
                ('ocurrence_time', models.TimeField(help_text='Hora da ocorrência')),
                ('description_ocurrence', models.TextField(help_text='Descrição da ocorrência')),
                ('immediate_action', models.TextField(help_text='O que foi realizado após a corrência / Ação imediata')),
                ('damage_classification', models.ForeignKey(help_text='Classificação do Dano', on_delete=django.db.models.deletion.DO_NOTHING, related_name='damage_events', to='classifications.damageclassification')),
                ('incident_classification', models.ForeignKey(help_text='Classificação do Incidente', on_delete=django.db.models.deletion.DO_NOTHING, related_name='incident_events', to='classifications.incidentclassification')),
                ('notified_department', models.ForeignKey(help_text='Setor que está sendo notificado', on_delete=django.db.models.deletion.DO_NOTHING, related_name='notified_events', to='departments.department')),
                ('ocurrence_classification', models.ForeignKey(help_text='Classificação da Ocorrência', on_delete=django.db.models.deletion.DO_NOTHING, related_name='ocurrence_events', to='classifications.ocurrenceclassification')),
                ('reporting_department', models.ForeignKey(help_text='Setor que está reportando', on_delete=django.db.models.deletion.DO_NOTHING, related_name='reporting_events', to='departments.department')),
            ],
            options={
                'verbose_name': 'Ocorrência',
                'verbose_name_plural': 'Ocorrências',
                'ordering': ['created_at'],
                'indexes': [models.Index(fields=['patient_involved'], name='events_even_patient_b6b9d1_idx'), models.Index(fields=['ocurrence_date'], name='events_even_ocurren_6fa75d_idx'), models.Index(fields=['reporting_department'], name='events_even_reporti_66644f_idx'), models.Index(fields=['notified_department'], name='events_even_notifie_1b9ac4_idx'), models.Index(fields=['incident_classification'], name='events_even_inciden_b02e4a_idx'), models.Index(fields=['ocurrence_classification'], name='events_even_ocurren_034e96_idx'), models.Index(fields=['damage_classification'], name='events_even_damage__535a6b_idx')],
            },
        ),
    ]