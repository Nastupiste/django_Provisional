# Generated by Django 3.2.22 on 2024-01-11 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provisional', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='modelo',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=150),
        ),
    ]