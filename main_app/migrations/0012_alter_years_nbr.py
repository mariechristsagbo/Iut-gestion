# Generated by Django 5.0.5 on 2024-05-08 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_student_years_alter_years_nbr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='years',
            name='nbr',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=5),
        ),
    ]
