# Generated by Django 4.0.5 on 2022-06-06 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_language_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text='jkdsbjfsk', to='catalog.genre'),
        ),
    ]
