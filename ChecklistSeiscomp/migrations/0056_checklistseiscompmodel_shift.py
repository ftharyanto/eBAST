# Generated by Django 4.2.4 on 2023-10-01 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChecklistSeiscomp', '0055_remove_checklistseiscompmodel_shift'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklistseiscompmodel',
            name='shift',
            field=models.CharField(default='', max_length=20),
        ),
    ]
