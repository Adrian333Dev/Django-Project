# Generated by Django 4.2.3 on 2023-07-23 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_room_host'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['-updated', '-created']},
        ),
    ]
