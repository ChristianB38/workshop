# Generated by Django 4.2.17 on 2025-01-10 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='star',
            name='discovered_by',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
