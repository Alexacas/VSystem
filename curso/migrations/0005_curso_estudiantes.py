# Generated by Django 5.1.1 on 2024-10-12 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0004_rename_profesor_id_curso_profesor'),
        ('persona', '0003_alter_persona_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='estudiantes',
            field=models.ManyToManyField(blank=True, related_name='cursos_estudiante', to='persona.persona'),
        ),
    ]
