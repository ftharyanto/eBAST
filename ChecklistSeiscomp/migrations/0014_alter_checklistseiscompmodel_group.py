# Generated by Django 4.0.6 on 2023-03-09 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChecklistSeiscomp', '0013_alter_checklistseiscompmodel_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklistseiscompmodel',
            name='group',
            field=models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3')], null=True),
        ),
    ]