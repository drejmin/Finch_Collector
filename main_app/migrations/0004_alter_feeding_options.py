# Generated by Django 4.2.4 on 2023-08-15 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_toy_finch_age_finch_breed_finch_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feeding',
            options={'ordering': ['-date']},
        ),
    ]
