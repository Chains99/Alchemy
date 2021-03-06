# Generated by Django 3.2 on 2021-10-17 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('imparts', '0001_initial'),
        ('professors', '0001_initial'),
        ('subjects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imparts',
            name='professor',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='professors.professor'),
        ),
        migrations.AddField(
            model_name='imparts',
            name='subject',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='subjects.subject'),
        ),
        migrations.AlterUniqueTogether(
            name='imparts',
            unique_together={('professor', 'subject')},
        ),
    ]
