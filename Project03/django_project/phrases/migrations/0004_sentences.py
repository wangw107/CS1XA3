# Generated by Django 2.2 on 2019-04-24 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phrases', '0003_remove_phrases_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sentences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentence', models.CharField(max_length=256)),
            ],
        ),
    ]
