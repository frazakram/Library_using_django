# Generated by Django 4.0.5 on 2022-06-06 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_book_genre_alter_language_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='lanuage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chooselanuage', models.CharField(max_length=100)),
            ],
        ),
    ]
