# Generated by Django 4.0.6 on 2022-11-05 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_panel_7c_icono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='panel_7c',
            name='fondo',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='panel_7c',
            name='icono',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='panel_7c',
            name='logo',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='programa',
            name='galeria_1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='programa',
            name='galeria_2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='programa',
            name='galeria_3',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='programa',
            name='galeria_4',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='programa',
            name='galeria_5',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='programa',
            name='galeria_6',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='programa',
            name='icono',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='programa',
            name='portada',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='programa',
            name='tecnologias_icono',
            field=models.TextField(blank=True, null=True),
        ),
    ]
