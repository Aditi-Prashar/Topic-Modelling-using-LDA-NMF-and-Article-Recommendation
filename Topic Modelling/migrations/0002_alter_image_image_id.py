# Generated by Django 4.1.7 on 2023-03-23 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topicmodelling', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
