# Generated by Django 4.0.4 on 2022-05-04 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_alter_topic_topictitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='themeTitle',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
    ]
