# Generated by Django 4.1.3 on 2022-12-04 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Fly', '0002_team'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Universe',
            new_name='Aircraft',
        ),
        migrations.DeleteModel(
            name='Team',
        ),
    ]
