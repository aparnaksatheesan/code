# Generated by Django 4.1.3 on 2022-12-03 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fly', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='photos')),
                ('description', models.TextField()),
            ],
        ),
    ]
