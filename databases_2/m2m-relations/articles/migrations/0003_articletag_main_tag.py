# Generated by Django 3.1.2 on 2022-01-04 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20220104_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='articletag',
            name='main_tag',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
