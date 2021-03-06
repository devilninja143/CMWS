# Generated by Django 3.1.4 on 2021-01-14 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_cvimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workhistory',
            name='companyName',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='workhistory',
            name='employmentDateEnd',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='workhistory',
            name='employmentDateStart',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='workhistory',
            name='jobTitle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
