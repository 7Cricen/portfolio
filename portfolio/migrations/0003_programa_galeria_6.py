# Generated by Django 4.0.6 on 2022-11-02 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_programa_galeria_1_programa_galeria_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='programa',
            name='galeria_6',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
