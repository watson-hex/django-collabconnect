# Generated by Django 3.2.10 on 2022-01-21 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0039_auto_20220121_0106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competition',
            name='disabled',
        ),
        migrations.AddField(
            model_name='club',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='competition',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
