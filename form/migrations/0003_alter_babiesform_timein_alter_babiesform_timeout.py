# Generated by Django 5.0.3 on 2024-04-18 11:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_alter_babiesform_timein_alter_babiesform_timeout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='babiesform',
            name='timein',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='babiesform',
            name='timeout',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]