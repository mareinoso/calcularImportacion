from django.db import models
from django.core.validators import MinValueValidator, MinLengthValidator, MaxLengthValidator
# Create your models here.
class Importacion(models.Model):
    codigo_producto = models.CharField(max_length = 50, validators=[MinLengthValidator(1, message="Escriba un codigo valido"), MaxLengthValidator(50, message="El codigo debe tener menos de 50 caracteres")])
    nombre_producto = models.CharField(max_length = 100, validators=[MinLengthValidator(2, message="Escriba un nombre valido"), MaxLengthValidator(100, message="El nombre debe tener menos de 100 caracteres")])
    proveedor = models.CharField(max_length = 50, validators=[MinLengthValidator(2, message="Escriba un nombre valido"), MaxLengthValidator(50, message="El nombre debe tener menos de 50 caracteres")])

    valor_unidad_usd = models.FloatField(validators=[MinValueValidator(0, message="El valor no debe ser negativo")])
    cantidad = models.IntegerField(validators=[MinValueValidator(1, message="La cantidad no puede ser menor a 1")])
    valor_productos_clp = models.IntegerField()
    valor_envio_usd = models.IntegerField(validators=[MinValueValidator(0, message="El valor no debe ser negativo")])
    iva_clp = models.IntegerField()
    aduana_clp = models.IntegerField()
    total_importacion_clp = models.IntegerField()
    total_importacion_usd = models.FloatField()

    valor_unidad_clp = models.IntegerField()
    valor_productos_usd = models.FloatField()
    valor_cif_usd = models.FloatField()
    valor_envio_clp = models.IntegerField()
    valor_cif_clp = models.IntegerField()
    iva_usd = models.FloatField()
    aduana_usd = models.FloatField()

    # null=False, blank=False