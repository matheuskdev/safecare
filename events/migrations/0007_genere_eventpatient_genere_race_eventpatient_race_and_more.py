# Generated by Django 5.1.1 on 2024-11-05 12:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_alter_ocurrencedescription_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(help_text='Gênero', max_length=255)),
            ],
            options={
                'verbose_name': 'Gênero',
                'verbose_name_plural': 'Gêneros',
                'ordering': ['name'],
                'indexes': [models.Index(fields=['name'], name='events_gene_name_e7ceae_idx')],
            },
        ),
        migrations.AddField(
            model_name='eventpatient',
            name='genere',
            field=models.ForeignKey(blank=True, help_text='Gênero', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='event_genere', to='events.genere'),
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(help_text='Raça', max_length=255)),
            ],
            options={
                'verbose_name': 'Raça',
                'verbose_name_plural': 'Raças',
                'ordering': ['name'],
                'indexes': [models.Index(fields=['name'], name='events_race_name_fadc17_idx')],
            },
        ),
        migrations.AddField(
            model_name='eventpatient',
            name='race',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='event_race', to='events.race'),
        ),
        migrations.AddIndex(
            model_name='eventpatient',
            index=models.Index(fields=['genere'], name='events_even_genere__eb75c9_idx'),
        ),
        migrations.AddIndex(
            model_name='eventpatient',
            index=models.Index(fields=['race'], name='events_even_race_id_b10d79_idx'),
        ),
    ]
