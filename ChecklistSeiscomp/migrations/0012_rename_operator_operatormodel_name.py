# Generated by Django 4.0.6 on 2023-03-08 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChecklistSeiscomp', '0011_rename_operator_operatormodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='operatormodel',
            old_name='operator',
            new_name='name',
        ),
    ]