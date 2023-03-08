# Generated by Django 4.0.6 on 2023-03-08 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChecklistSeiscomp', '0006_remove_checklistseiscompmodel_blanks_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklistseiscompmodel',
            name='blanks',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='checklistseiscompmodel',
            name='gaps',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='checklistseiscompmodel',
            name='operator',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='checklistseiscompmodel',
            name='spikes',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
