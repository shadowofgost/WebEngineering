# Generated by Django 3.0 on 2021-03-17 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20210317_2254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tcyuser',
            name='back_up4',
        ),
        migrations.RemoveField(
            model_name='tcyuserex',
            name='back_up',
        ),
        migrations.AddField(
            model_name='tcyuser',
            name='back_up1',
            field=models.CharField(blank=True, default='1', max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='tcyuserex',
            name='back_up1',
            field=models.CharField(blank=True, default='1', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='tcycurricula',
            name='back_up2',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='tcycurricula',
            name='back_up3',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='tcycurricula',
            name='bakc_up1',
            field=models.CharField(blank=True, default='1', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='tcydept',
            name='back_up2',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='tcydept',
            name='bakc_up1',
            field=models.CharField(blank=True, default='1', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='tcyequipment',
            name='back_up1',
            field=models.CharField(blank=True, default='1', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='tcyequipment',
            name='back_up2',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='tcyequipment',
            name='back_up3',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='tcylocation',
            name='back_up1',
            field=models.CharField(blank=True, default='1', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='tcylocation',
            name='back_up2',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='tcylocation',
            name='back_up3',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='tcylocationex',
            name='back_up1',
            field=models.CharField(blank=True, default='1', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='tcylocationex',
            name='back_up2',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='tcylocationex',
            name='back_up3',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='tcymmx',
            name='back_up1',
            field=models.CharField(blank=True, default='1', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='tcymmx',
            name='back_up2',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='tcymmxdata',
            name='back_up1',
            field=models.CharField(blank=True, default='1', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='tcymmxdata',
            name='back_up2',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='tcyplan',
            name='back_up1',
            field=models.CharField(blank=True, default='1', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='tcyplan',
            name='back_up2',
            field=models.CharField(blank=True, default='1', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='tcyplan',
            name='back_up3',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='tcyplan',
            name='back_up4',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='tcyrunningaccount',
            name='back_up1',
            field=models.CharField(blank=True, default='1', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='tcyrunningaccount',
            name='back_up2',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='tcyrunningaccount',
            name='back_up3',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='tcytableinfo',
            name='back_up1',
            field=models.CharField(blank=True, default='1', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='tcytableinfo',
            name='back_up2',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='tcytableinfo',
            name='back_up3',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='tcytypera',
            name='back_up1',
            field=models.CharField(blank=True, default='1', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='tcytypera',
            name='back_up2',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='tcyuser',
            name='back_up2',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='tcyuser',
            name='back_up3',
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name='tcyuserex',
            name='back_up2',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='tcyuserex',
            name='back_up3',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
