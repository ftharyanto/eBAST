# Generated by Django 4.0.6 on 2023-03-08 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChecklistSeiscomp', '0010_checklistseiscompmodel_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Operator',
            new_name='OperatorModel',
        ),
    ]
