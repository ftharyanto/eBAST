# Generated by Django 4.0.6 on 2023-03-07 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChecklistSeiscomp', '0002_rename_checklistsmodel_checklistseiscompmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklistseiscompmodel',
            name='blanks',
            field=models.JSONField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='checklistseiscompmodel',
            name='gaps',
            field=models.JSONField(default='', null=True),
        ),
        migrations.AlterField(
            model_name='checklistseiscompmodel',
            name='spikes',
            field=models.JSONField(default='', null=True),
        ),
    ]