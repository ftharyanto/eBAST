# Generated by Django 4.0.6 on 2023-03-08 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChecklistSeiscomp', '0012_rename_operator_operatormodel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklistseiscompmodel',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='checklistseiscompmodel',
            name='group',
            field=models.IntegerField(null=True),
        ),
    ]