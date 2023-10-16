# Generated by Django 4.2.4 on 2023-10-15 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Importacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_producto', models.CharField(max_length=50)),
                ('nombre_producto', models.CharField(max_length=100)),
                ('proveedor', models.CharField(max_length=100)),
                ('valor_unidad_usd', models.FloatField()),
                ('cantidad', models.IntegerField()),
                ('valor_productos_clp', models.IntegerField()),
                ('valor_envio_usd', models.IntegerField()),
                ('iva_clp', models.IntegerField()),
                ('aduana_clp', models.IntegerField()),
                ('total_importacion_clp', models.IntegerField()),
                ('total_importacion_usd', models.FloatField()),
                ('valor_unidad_clp', models.IntegerField()),
                ('valor_productos_usd', models.FloatField()),
                ('valor_cif_usd', models.FloatField()),
                ('valor_envio_clp', models.IntegerField()),
                ('valor_cif_clp', models.IntegerField()),
                ('iva_usd', models.FloatField()),
                ('aduana_usd', models.FloatField()),
            ],
        ),
    ]
