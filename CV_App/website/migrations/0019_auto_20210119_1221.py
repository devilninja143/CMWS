# Generated by Django 3.1.4 on 2021-01-19 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_cvinfo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cvimg',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to='media'),
        ),
    ]