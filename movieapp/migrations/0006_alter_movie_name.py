# Generated by Django 4.0.3 on 2022-11-28 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0005_alter_movie_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
    ]
