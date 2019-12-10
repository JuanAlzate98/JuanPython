# Generated by Django 2.2 on 2019-10-30 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EstaCivil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreEsta', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Estado Civil',
                'verbose_name_plural': 'Estado civil',
            },
        ),
        migrations.CreateModel(
            name='Etnia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreEtni', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Grupo Etnico',
                'verbose_name_plural': 'Grupos Etnicos',
            },
        ),
        migrations.CreateModel(
            name='TipoDocu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreTiDo', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Tipo De Documento',
                'verbose_name_plural': 'Tipo De Documentos',
            },
        ),
        migrations.CreateModel(
            name='TipoLogr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NombreTiLo', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Tipo De Logro',
                'verbose_name_plural': 'Tipo De Logros',
            },
        ),
    ]
