# Generated by Django 4.1.7 on 2023-04-09 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChecklistSeiscomp', '0044_stationlistmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stationlistmodel',
            old_name='stasiun',
            new_name='lokasi',
        ),
    ]
