# Generated by Django 2.2 on 2019-04-23 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phrases', '0002_phrases_index'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phrases',
            name='index',
        ),
    ]