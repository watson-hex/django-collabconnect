# Generated by Django 3.2.2 on 2021-05-12 14:16

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=30)),
                ('Last_Name', models.CharField(blank=True, max_length=30)),
                ('Gender', models.CharField(blank=True, default=None, max_length=1)),
                ('Degree', models.CharField(blank=True, max_length=1)),
                ('Course', models.CharField(blank=True, max_length=10)),
                ('Email', models.EmailField(max_length=50, unique=True)),
                ('Handle', models.CharField(blank=True, default=None, max_length=50)),
                ('IsTeacher', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('Teacher_set', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30), size=2), size=5)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.OneToOneField(max_length=6, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='connect.profile', verbose_name='ID')),
                ('Skill_set', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=30), blank=True, default=list, null=True, size=2), blank=True, default=list, null=True, size=5)),
                ('Contact', models.BigIntegerField(unique=True)),
            ],
        ),
    ]
