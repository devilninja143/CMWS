# Generated by Django 3.1.4 on 2021-01-19 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_auto_20210119_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cvimg',
            name='img',
            field=models.FileField(blank=True, default='/media/avatar.png', null=True, upload_to='media'),
        ),
    ]
