# Generated by Django 4.0.6 on 2023-03-18 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChecklistSeiscomp', '0020_alter_checklistseiscompmodel_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklistseiscompmodel',
            name='time',
            field=models.CharField(choices=[(1, '12:00 WIB'), (2, '00:00 WIB')], default=1, max_length=50),
        ),
    ]