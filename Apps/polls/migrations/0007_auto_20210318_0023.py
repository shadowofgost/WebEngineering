# Generated by Django 3.0 on 2021-03-18 00:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20210317_2334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tcycurricula',
            name='id_location',
            field=models.ForeignKey(db_column='ID_Location', on_delete=django.db.models.deletion.CASCADE, related_name='curricula_related_to_location', to='polls.TCylocation'),
        ),
        migrations.AlterField(
            model_name='tcycurricula',
            name='id_speaker',
            field=models.ForeignKey(db_column='ID_Speaker', on_delete=django.db.models.deletion.CASCADE, related_name='curricula_related_to_user_speaker', to='polls.TCyuser'),
        ),
        migrations.AlterField(
            model_name='tcycurricula',
            name='idmanager',
            field=models.ForeignKey(db_column='IdManager', on_delete=django.db.models.deletion.CASCADE, related_name='curricula_related_to_user', to='polls.TCyuser'),
        ),
        migrations.AlterField(
            model_name='tcyequipment',
            name='id_location',
            field=models.ForeignKey(db_column='ID_Location', on_delete=django.db.models.deletion.CASCADE, related_name='equipment_related_to_location', to='polls.TCylocation'),
        ),
        migrations.AlterField(
            model_name='tcyequipment',
            name='id_plan',
            field=models.ForeignKey(db_column='ID_Plan', on_delete=django.db.models.deletion.CASCADE, related_name='equipment_related_to_plan', to='polls.TCyplan'),
        ),
        migrations.AlterField(
            model_name='tcyequipment',
            name='id_user',
            field=models.ForeignKey(db_column='ID_User', on_delete=django.db.models.deletion.CASCADE, related_name='equipment_related_to_user_use', to='polls.TCyuser'),
        ),
        migrations.AlterField(
            model_name='tcyequipment',
            name='idmanager',
            field=models.ForeignKey(db_column='IdManager', on_delete=django.db.models.deletion.CASCADE, related_name='equipment_related_to_user', to='polls.TCyuser'),
        ),
        migrations.AlterField(
            model_name='tcylocation',
            name='idmanager',
            field=models.ForeignKey(db_column='IdManager', on_delete=django.db.models.deletion.CASCADE, related_name='location_related_to_user', to='polls.TCyuser'),
        ),
        migrations.AlterField(
            model_name='tcylocationex',
            name='idmanager',
            field=models.ForeignKey(db_column='IdManager', on_delete=django.db.models.deletion.CASCADE, related_name='locationex_related_to_user', to='polls.TCyuser'),
        ),
        migrations.AlterField(
            model_name='tcymmx',
            name='idmanager',
            field=models.ForeignKey(db_column='IdManager', on_delete=django.db.models.deletion.CASCADE, related_name='mmx_related_to_user', to='polls.TCyuser'),
        ),
        migrations.AlterField(
            model_name='tcymmxdata',
            name='idmanager',
            field=models.ForeignKey(db_column='IdManager', on_delete=django.db.models.deletion.CASCADE, related_name='mmxdata_related_to_user', to='polls.TCyuser'),
        ),
        migrations.AlterField(
            model_name='tcyplan',
            name='id_curricula',
            field=models.ForeignKey(db_column='ID_Curricula', on_delete=django.db.models.deletion.CASCADE, related_name='plan_related_to_curricula', to='polls.TCycurricula'),
        ),
        migrations.AlterField(
            model_name='tcyplan',
            name='id_location',
            field=models.ForeignKey(db_column='ID_Location', on_delete=django.db.models.deletion.CASCADE, related_name='plan_related_to_location', to='polls.TCylocation'),
        ),
        migrations.AlterField(
            model_name='tcyplan',
            name='id_speaker',
            field=models.ForeignKey(db_column='ID_Speaker', on_delete=django.db.models.deletion.CASCADE, related_name='plan_related_to_user_speaker', to='polls.TCyuser'),
        ),
        migrations.AlterField(
            model_name='tcyplan',
            name='idmanager',
            field=models.ForeignKey(db_column='IdManager', on_delete=django.db.models.deletion.CASCADE, related_name='plan_related_to_user', to='polls.TCyuser'),
        ),
        migrations.AlterField(
            model_name='tcyrunningaccount',
            name='id_user',
            field=models.ForeignKey(db_column='ID_User', on_delete=django.db.models.deletion.CASCADE, related_name='runningaccount_related_to_user_use', to='polls.TCyuser'),
        ),
        migrations.AlterField(
            model_name='tcyrunningaccount',
            name='idmanager',
            field=models.ForeignKey(db_column='IdManager', on_delete=django.db.models.deletion.CASCADE, related_name='runningaccount_related_to_user', to='polls.TCyuser'),
        ),
        migrations.AlterField(
            model_name='tcytableinfo',
            name='idmanager',
            field=models.ForeignKey(db_column='IdManager', on_delete=django.db.models.deletion.CASCADE, related_name='kaoqin_related_to_user', to='polls.TCyuser'),
        ),
        migrations.AlterField(
            model_name='tcytypera',
            name='id',
            field=models.IntegerField(blank=True, db_column='ID', default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tcytypera',
            name='idmanager',
            field=models.ForeignKey(db_column='IdManager', on_delete=django.db.models.deletion.CASCADE, related_name='typera_related_to_user', to='polls.TCyuser'),
        ),
        migrations.AlterField(
            model_name='tcyuser',
            name='deptid',
            field=models.ForeignKey(db_column='Deptid', on_delete=django.db.models.deletion.CASCADE, related_name='related_to_department', to='polls.TCydept'),
        ),
        migrations.AlterField(
            model_name='tcyuserex',
            name='idmanager',
            field=models.ForeignKey(db_column='IdManager', on_delete=django.db.models.deletion.CASCADE, related_name='userex_related_to_user', to='polls.TCyuser'),
        ),
    ]