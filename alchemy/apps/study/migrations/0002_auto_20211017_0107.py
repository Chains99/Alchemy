# Generated by Django 3.2 on 2021-10-17 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0001_initial'),
        ('students', '0001_initial'),
        ('study', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study',
            name='student',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='students.student'),
        ),
        migrations.AlterField(
            model_name='study',
            name='subject',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='subjects.subject'),
        ),
    ]
