# Generated by Django 3.2 on 2021-10-17 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('non_basic_elements', '0001_initial'),
        ('study', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nonbasicelement',
            name='study',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='nonBasicElement_study', to='study.study'),
        ),
    ]