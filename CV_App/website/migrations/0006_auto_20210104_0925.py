# Generated by Django 3.1.4 on 2021-01-04 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20210104_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personalaccomplishment',
            name='paccomplishment1',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='personalaccomplishment',
            name='paccomplishment2',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='personalaccomplishment',
            name='paccomplishment3',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='personalaccomplishment',
            name='paccomplishment4',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='personalaccomplishment',
            name='paccomplishment5',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='professionalaccomplishment',
            name='praccomplishment1',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='professionalaccomplishment',
            name='praccomplishment2',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='professionalaccomplishment',
            name='praccomplishment3',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='professionalaccomplishment',
            name='praccomplishment4',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='professionalaccomplishment',
            name='praccomplishment5',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
