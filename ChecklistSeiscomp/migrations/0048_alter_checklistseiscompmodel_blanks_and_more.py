# Generated by Django 4.2.4 on 2023-09-30 12:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChecklistSeiscomp', '0047_alter_checklistseiscompmodel_blanks_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklistseiscompmodel',
            name='blanks',
            field=models.TextField(blank=True, default='', max_length=500, validators=[django.core.validators.MaxLengthValidator(500)]),
        ),
        migrations.AlterField(
            model_name='checklistseiscompmodel',
            name='gaps',
            field=models.TextField(blank=True, default='', max_length=500, validators=[django.core.validators.MaxLengthValidator(500)]),
        ),
        migrations.AlterField(
            model_name='checklistseiscompmodel',
            name='spikes',
            field=models.TextField(blank=True, default='', max_length=500, validators=[django.core.validators.MaxLengthValidator(500)]),
        ),
    ]