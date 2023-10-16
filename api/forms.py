from django import forms
from .models import Importacion

class AgregarForm(forms.ModelForm):
    class Meta:
        model = Importacion
        fields = '__all__'
        labels = {'codigo_producto': "Codigo del producto",
                  'nombre_producto': "Nombre del producto",
                  'proveedor': "Nombre del proveedor",
                  'valor_unidad_usd': "Valor del producto (USD)",
                  'valor_productos_clp': "Precio por productos (CLP) - autocompletado",
                  'valor_envio_usd': "Precio de envío (USD)",
                  'iva_clp': "Impuesto IVA (CLP) - autocompletado",
                  'aduana_clp': "Impuesto aduana (CLP) - autocompletado",
                  'total_importacion_usd': "Costo total en USD - autocompletado",
                  'total_importacion_clp': "Costo total en CLP - autocompletado",
                  }
        
        
        widgets = {'codigo_producto' : forms.TextInput(attrs={'class' : 'form-control'}),
                   'nombre_producto' : forms.TextInput(attrs={'class' : 'form-control'}),
                   'proveedor' : forms.TextInput(attrs={'class' : 'form-control'}),
                   'valor_unidad_usd' : forms.NumberInput(attrs={'onchange': 'calcularTotalPedido();', 'min_value': 0, 'class' : 'form-control'}),
                   'cantidad' : forms.NumberInput(attrs={'onchange': 'calcularTotalPedido();', 'value': 1, 'min_value': 1, 'class' : 'form-control'}),
                   'valor_productos_clp' : forms.NumberInput(attrs={'readonly' : 'readonly', 'class' : 'form-control bg-light'}),
                   'valor_envio_usd' : forms.NumberInput(attrs={'onchange': 'calcularEnvio();', 'min_value': 0, 'class' : 'form-control'}),
                   'iva_clp' : forms.NumberInput(attrs={'readonly' : 'readonly', 'class' : 'form-control bg-light'}),
                   'aduana_clp' : forms.NumberInput(attrs={'readonly' : 'readonly', 'class' : 'form-control bg-light'}),
                   'total_importacion_clp' : forms.NumberInput(attrs={'readonly' : 'readonly', 'class' : 'form-control bg-light'}),
                   'total_importacion_usd' : forms.NumberInput(attrs={'readonly' : 'readonly', 'class' : 'form-control bg-light'}),
                   'valor_unidad_clp' : forms.HiddenInput(),
                   'valor_productos_usd' : forms.HiddenInput(),
                   'valor_envio_clp' : forms.HiddenInput(),
                   'valor_cif_usd' : forms.HiddenInput(),
                   'valor_cif_clp' : forms.HiddenInput(),
                   'iva_usd' : forms.HiddenInput(),
                   'aduana_usd' : forms.HiddenInput()
                   }
                   