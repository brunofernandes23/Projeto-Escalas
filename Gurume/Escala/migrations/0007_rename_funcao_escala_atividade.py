# Generated by Django 4.0.5 on 2022-06-15 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Escala', '0006_alter_escala_praca'),
    ]

    operations = [
        migrations.RenameField(
            model_name='escala',
            old_name='funcao',
            new_name='atividade',
        ),
    ]