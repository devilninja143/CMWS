# Generated by Django 3.1.4 on 2021-01-06 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20210104_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cvinfo',
            name='objective',
            field=models.TextField(default='I am seeking employment with a company where I can grow professionally and personally.I seek challenging opportunities where I can fully use my skills for the success of the organization.With the sill sets that I have I am very confident that I am perfect for this job.'),
        ),
    ]