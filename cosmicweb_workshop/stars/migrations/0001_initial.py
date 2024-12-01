# Generated by Django 4.2.16 on 2024-12-01 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('constellation', models.CharField(max_length=100)),
                ('magnitude', models.FloatField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
