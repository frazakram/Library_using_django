# Generated by Django 4.0.5 on 2022-06-06 22:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_delete_authoradmin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='language',
        ),
    ]
