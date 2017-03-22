# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-21 12:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChemicalElement',
            fields=[
                ('code', models.CharField(max_length=2, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Mineral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('category', models.CharField(max_length=255)),
                ('image_caption', models.TextField()),
                ('image_filename', models.CharField(blank=True, max_length=255)),
                ('group', models.CharField(max_length=255)),
                ('formula', models.TextField(blank=True)),
                ('strunz_classification', models.CharField(blank=True, max_length=255)),
                ('crystal_system', models.CharField(blank=True, max_length=255)),
                ('mohs_scale_hardness', models.CharField(blank=True, max_length=255)),
                ('luster', models.CharField(blank=True, max_length=255)),
                ('color', models.CharField(blank=True, max_length=255)),
                ('specific_gravity', models.CharField(blank=True, max_length=255)),
                ('cleavage', models.CharField(blank=True, max_length=255)),
                ('diaphaneity', models.CharField(blank=True, max_length=255)),
                ('crystal_habit', models.CharField(blank=True, max_length=255)),
                ('streak', models.CharField(blank=True, max_length=255)),
                ('optical_properties', models.CharField(blank=True, max_length=255)),
                ('refractive_index', models.CharField(blank=True, max_length=255)),
                ('unit_cell', models.CharField(blank=True, max_length=255)),
                ('crystal_symmetry', models.CharField(blank=True, max_length=255)),
            ],
            options={
                'ordering': ['name'],
            },
            managers=[
                ('minerals', django.db.models.manager.Manager()),
            ],
        ),
    ]
