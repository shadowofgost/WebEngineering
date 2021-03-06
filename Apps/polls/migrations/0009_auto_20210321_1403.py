# Generated by Django 3.0 on 2021-03-21 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20210318_0211'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tcyrunningaccount',
            old_name='type',
            new_name='type_field',
        ),
        migrations.AlterField(
            model_name='tcyplan',
            name='id_curricula',
            field=models.ForeignKey(db_column='ID_Curricula', on_delete=django.db.models.deletion.CASCADE, related_name='id_curricula', to='polls.TCycurricula'),
        ),
    ]
