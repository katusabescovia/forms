# Generated by Django 4.2.11 on 2024-04-19 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0003_alter_babiesform_timein_alter_babiesform_timeout'),
    ]

    operations = [
        migrations.AddField(
            model_name='babiesform',
            name='name_of_the_person_taken_the_baby',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
