# Generated by Django 5.1.1 on 2024-10-21 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='damageclassification',
            options={'ordering': ['classification'], 'verbose_name': 'Classificação de Dano', 'verbose_name_plural': 'Classificações dos Danos'},
        ),
        migrations.AlterModelOptions(
            name='incidentclassification',
            options={'ordering': ['classification'], 'verbose_name': 'Classificação de Incidente', 'verbose_name_plural': 'Classificações dos Incidentes'},
        ),
        migrations.AlterModelOptions(
            name='ocurrenceclassification',
            options={'ordering': ['classification'], 'verbose_name': 'Classificação de Ocorrência', 'verbose_name_plural': 'Classificações das Ocorrências'},
        ),
    ]
