# Generated by Django 5.1.1 on 2024-10-02 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0003_remove_curso_id_curso'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='profesor_id',
            new_name='profesor',
        ),
    ]
