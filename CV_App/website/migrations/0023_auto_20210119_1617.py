# Generated by Django 3.1.4 on 2021-01-19 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0022_auto_20210119_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cvimg',
            name='img',
            field=models.FileField(blank=True, default='/media/media/avatar.png', null=True, upload_to='media'),
        ),
    ]