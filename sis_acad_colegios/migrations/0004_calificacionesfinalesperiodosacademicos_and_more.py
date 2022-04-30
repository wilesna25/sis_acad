# Generated by Django 4.0.4 on 2022-04-29 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sis_acad_colegios', '0003_alter_conceptosacademicos_nota_maxima_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CalificacionesFinalesPeriodosAcademicos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calificacionFinal', models.FloatField(null=True)),
                ('nivelDesempeno', models.CharField(max_length=50, null=True)),
                ('clase', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sis_acad_colegios.clases')),
                ('estudiante', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sis_acad_colegios.estudiantes')),
                ('periodoAcademico', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sis_acad_colegios.periodoacademico')),
            ],
            options={
                'verbose_name': 'Calificacion final periodo académico.',
                'verbose_name_plural': 'Calificaiones finales periodo académico',
            },
        ),
        migrations.CreateModel(
            name='CalificacionesPeriodoAcademico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo_academico', models.IntegerField(null=True)),
                ('calificacion_1', models.FloatField(null=True)),
                ('calificacion_2', models.FloatField(null=True)),
                ('calificacion_3', models.FloatField(null=True)),
                ('calificacion_4', models.FloatField(null=True)),
                ('calificacion_5', models.FloatField(null=True)),
                ('calificacion_6', models.FloatField(null=True)),
                ('calificacion_7', models.FloatField(null=True)),
                ('heteroevaluacion', models.FloatField(null=True)),
                ('examenBimestral', models.FloatField(null=True)),
                ('autoevaluacion', models.FloatField(null=True)),
                ('coevaluacion', models.FloatField(null=True)),
                ('clase', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sis_acad_colegios.clases')),
                ('estudiante', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sis_acad_colegios.estudiantes')),
            ],
            options={
                'verbose_name': 'Calificación',
                'verbose_name_plural': 'Calificaciones',
            },
        ),
        migrations.DeleteModel(
            name='Ciudades',
        ),
        migrations.DeleteModel(
            name='Departamentos',
        ),
    ]