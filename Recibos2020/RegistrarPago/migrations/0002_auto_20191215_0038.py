# Generated by Django 3.0 on 2019-12-15 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Recibo', '0001_initial'),
        ('RegistrarPago', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrarpagoagua',
            name='Estado',
            field=models.BooleanField(default=True, verbose_name='Estado del pago'),
        ),
        migrations.AddField(
            model_name='registrarpagocuarto',
            name='Estado',
            field=models.BooleanField(default=True, verbose_name='Estado del pago'),
        ),
        migrations.AddField(
            model_name='registrarpagoluz',
            name='Estado',
            field=models.BooleanField(default=True, verbose_name='Estado del pago'),
        ),
        migrations.AlterField(
            model_name='registrarpagocuarto',
            name='Codigo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Recibo.Cuarto', verbose_name='Numero o Codigo del cuarto  '),
        ),
    ]
