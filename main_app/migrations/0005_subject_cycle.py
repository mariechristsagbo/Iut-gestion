# Generated by Django 5.0.5 on 2024-05-07 15:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_student_cycle'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='cycle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.cycle'),
        ),
    ]
