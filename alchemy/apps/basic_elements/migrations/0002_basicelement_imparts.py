# Generated by Django 3.2 on 2021-10-17 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('imparts', '0001_initial'),
        ('basic_elements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicelement',
            name='imparts',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='basicElement_imparts', to='imparts.imparts'),
        ),
    ]
