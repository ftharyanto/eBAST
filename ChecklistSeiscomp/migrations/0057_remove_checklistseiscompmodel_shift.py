# Generated by Django 4.2.4 on 2023-10-01 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ChecklistSeiscomp', '0056_checklistseiscompmodel_shift'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checklistseiscompmodel',
            name='shift',
        ),
    ]
