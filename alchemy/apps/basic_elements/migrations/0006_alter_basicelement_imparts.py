# Generated by Django 3.2 on 2021-11-20 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imparts', '0002_initial'),
        ('basic_elements', '0005_alter_basicelement_imparts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicelement',
            name='imparts',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='basicElement_imparts', to='imparts.imparts'),
        ),
    ]