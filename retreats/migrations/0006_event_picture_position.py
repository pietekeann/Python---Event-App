# Generated by Django 3.0 on 2020-05-25 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retreats', '0005_auto_20200525_2015'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='picture_position',
            field=models.CharField(default='center', max_length=6),
        ),
    ]
