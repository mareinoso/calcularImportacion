// contantes para calculos
const dolar_clp = 890;
const impuesto_iva = 0.19;
const impuesto_aduana = 0.06;

function calcularTotalPedido(){

  // Obtiene los valores por medio del id
  var cantidad = document.getElementById('id_cantidad').value;
  var valor_unidad_usd = document.getElementById('id_valor_unidad_usd').value;

  if (valor_unidad_usd <= 0 || cantidad < 1){
    return;
  }
  // Calcula el valor por los productos en clp
  var valor_unidad_clp = Math.round(valor_unidad_usd * dolar_clp);
  var valor_productos_clp = valor_unidad_clp * cantidad;

  //usd
  var valor_productos_usd = valor_unidad_usd * cantidad;

  // almacena y muestra los valores
  document.getElementById('id_valor_productos_clp').value = valor_productos_clp;

  //almacena en los hidden input
  document.getElementById('id_valor_unidad_clp').value = valor_unidad_clp;
  document.getElementById('id_valor_productos_usd').value = valor_productos_usd;


  // Comprueba si se debe de actualizar el los resultados del envio
  var valor_envio_usd = document.getElementById('id_valor_envio_usd').value;
  if (valor_envio_usd.length != 0){
    calcularEnvio();
  } 
}

function calcularEnvio(){
  // Obtiene los valores para realizar el calculo
  var valor_productos_clp = document.getElementById('id_valor_productos_clp').value;
  var valor_envio_usd = document.getElementById('id_valor_envio_usd').value;

  var valor_productos_usd = Math.round(valor_productos_clp / dolar_clp);

  if (valor_envio_usd < 0){
    alert("Valor ingresado no valido");
    return;
    }

  var valor_envio_clp = valor_envio_usd * dolar_clp;
 
  var valor_cif_clp = parseInt(valor_envio_clp) + parseInt(valor_productos_clp);
  var iva_clp = Math.round(valor_cif_clp * impuesto_iva);
  var aduana_clp = Math.round(valor_cif_clp * impuesto_aduana);
  var total_clp = valor_cif_clp + iva_clp + aduana_clp;

  var valor_cif_usd = parseInt(valor_envio_usd) + parseInt(valor_productos_usd);
  var iva_usd = (valor_cif_usd * impuesto_iva).toFixed(2);
  var aduana_usd = (valor_cif_usd * impuesto_aduana).toFixed(2);
  var total_usd = (valor_cif_usd + parseFloat(iva_usd) + parseFloat(aduana_usd)).toFixed(2);


  document.getElementById('id_iva_clp').value = iva_clp;
  document.getElementById('id_aduana_clp').value = aduana_clp;

  document.getElementById('id_total_importacion_clp').value = total_clp;
  document.getElementById('id_total_importacion_usd').value = total_usd;

  //Almacena los datos en los hidden input para subir a la base de datos
  document.getElementById('id_valor_envio_clp').value = valor_envio_clp;
  document.getElementById('id_valor_cif_clp').value = valor_cif_clp;
  document.getElementById('id_valor_cif_usd').value = valor_cif_usd;
  document.getElementById('id_iva_usd').value = iva_usd;
  document.getElementById('id_aduana_usd').value = aduana_usd;
}