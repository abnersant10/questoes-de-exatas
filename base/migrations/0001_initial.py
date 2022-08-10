# Generated by Django 4.1 on 2022-08-10 19:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('cod_area', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('nome_area', models.CharField(max_length=90)),
            ],
        ),
        migrations.CreateModel(
            name='Assunto',
            fields=[
                ('cod_assunto', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('assunto', models.CharField(max_length=90)),
                ('area_cod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.area')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('cod_curso', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('nome_curso', models.CharField(max_length=90)),
                ('area_cod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.area')),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('cod_disciplina', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('nome_disciplina', models.CharField(max_length=90)),
                ('area_cod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.area')),
                ('curso_cod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.curso')),
            ],
        ),
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('cod_questao', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('enunciado', models.TextField()),
                ('banca_examinadora', models.CharField(max_length=45)),
                ('ano_divulgacao', models.CharField(max_length=45)),
                ('area_cod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.area')),
                ('assunto_cod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.assunto')),
                ('curso_cod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.curso')),
            ],
        ),
        migrations.CreateModel(
            name='TetaUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teta', models.FloatField()),
                ('assunto_cod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.assunto')),
                ('disciplina_cod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.disciplina')),
                ('usuario', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='fk', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='QuestaoParametro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('A', models.TextField()),
                ('B', models.TextField()),
                ('C', models.TextField()),
                ('questao_cod', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.questao')),
            ],
        ),
        migrations.CreateModel(
            name='QuestaoAlternativa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('A', models.TextField()),
                ('B', models.TextField()),
                ('C', models.TextField()),
                ('D', models.TextField()),
                ('E', models.TextField()),
                ('gabarito', models.CharField(max_length=1)),
                ('questao_cod', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.questao')),
            ],
        ),
        migrations.AddField(
            model_name='assunto',
            name='curso_cod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.curso'),
        ),
        migrations.AddField(
            model_name='assunto',
            name='disciplina_cod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.disciplina'),
        ),
    ]
