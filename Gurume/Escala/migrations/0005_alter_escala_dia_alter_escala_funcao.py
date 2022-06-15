# Generated by Django 4.0.5 on 2022-06-14 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Escala', '0004_alter_escala_praca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='escala',
            name='dia',
            field=models.CharField(choices=[('Dom', 'Domingo'), ('Seg', 'Segunda'), ('Ter', 'Terça'), ('Qua', 'Quarta'), ('Qui', 'Quinta'), ('Sex', 'Sexta'), ('Sab', 'Sábado')], max_length=250),
        ),
        migrations.AlterField(
            model_name='escala',
            name='funcao',
            field=models.CharField(choices=[('Fol', 'Folga'), ('Pro', 'Produção'), ('Fin', 'Finalização'), ('Sla', 'Slash'), ('QA', 'QA'), ('Inv', 'Inventário'), ('Fec', 'Fechamento'), ('Alm', 'Almoço'), ('Jan', 'Janta')], max_length=250),
        ),
    ]