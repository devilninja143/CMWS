# Generated by Django 3.1.4 on 2021-01-04 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20210104_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cvinfo',
            name='cvEmail',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
