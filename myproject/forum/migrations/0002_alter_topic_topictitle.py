# Generated by Django 4.0.4 on 2022-05-04 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='topicTitle',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
    ]