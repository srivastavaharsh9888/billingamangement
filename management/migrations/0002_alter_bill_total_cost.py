# Generated by Django 4.2.7 on 2024-05-09 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='total_cost',
            field=models.FloatField(default=0.0, editable=False),
        ),
    ]