# Generated by Django 3.0.7 on 2021-06-01 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sis_acad_colegios', '0006_estudiantes_por_grupo'),
    ]

    operations = [
        migrations.CreateModel(
            name='falla_asistencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('justificada', models.BooleanField(default=False)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('clase', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sis_acad_colegios.Clases')),
                ('estudiante', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sis_acad_colegios.Estudiantes')),
                ('grupo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sis_acad_colegios.Grupos')),
            ],
        ),
    ]
