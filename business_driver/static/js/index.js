//Script de la pagina index.html
function filter_categorias(urls){
    $.ajax({
          type:'GET',
          url:urls,
          success:function(resp){
              $(".card-deck").html(resp);
          }
      });
  }
  function callData(urls,title){
      $.ajax({
          type:'GET',
          url:urls,
          success:function(resp){
              $(".modal-title").html(title)
              $(".modal-body").html(resp);
          }
      });
  }
$(document).ready(Sheart);
  function Sheart(){ 
    var tbuscar=$("#search-input");
    tbuscar.keypress(buscarProducto);
}
function buscarProducto(){
      $.ajax({
          type:'GET',
          url:'shear_tienda_view/',
          data:$("#search-input").serialize(),
          success:resultado,
          error:errores
      });
  }
$("#shear_form").on("submit",function(e){
  e.preventDefault();
  $.ajax({
    type:"POST",
    url:"shear_tienda_view/",
    data:$("#search-input").serialize(),
    success:resultado,
    error:errores
  });
});
function resultado(data){
  $(".card-deck").slideDown(1000);
  console.log(data);
  $(".card-deck").html(data).slideDown(5000);
}
function errores(){
  console.log("Error");
}
//script de la pagina SiteWeb_negocios.html
function ventana_modal(urls,title){
    $.ajax({
        type:'GET',
        url:urls,
        success:function(resp){
            $(".modal-title").html(title)
            $(".modal-body").html(resp);
        }
    });
}
//esta funcion aun no funciona
$('#hay_compra a').click(function(e){
e.preventDefault();
$.ajax({
        type:'GET',
        url:'registrar_cliente_orden/{{object.id}}',
        success:function(resp){
            $(".modal-title").html('otro')
            $(".modal-body").html(resp);
        }
    });
});
$('.card .card-body #form_pedido').submit(function(e){
  e.preventDefault();
  $.ajax({
        type:'POST',
        url:$(this).attr("action"),
        data:$(this).serialize(),
        success:function(resp){
          $("#compras_id").html(resp.total_compra);
          console.log(resp.datos);
          $("#datas").prepend("<a class='dropdown-item'><strong>"+resp.producto+ " </strong> Cant:  <strong>"+ resp.cantidad+"</strong> Precio Uni:  <strong> "+resp.precio_uni+" </strong> Total: <strong> "+resp.total+" </strong></a>");
          $("#id_Total_pagos").html(resp.total_pago);
          $(".toast .alert-success").html("Bien !!! agregaste:"+"<strong>"+resp.producto+"</strong>");
          $('.toast').toast({delay: 4000});
          $('.toast').toast('show');
          //$("#hay_compra").html("<a class='dropdown-item' id='hay' href='registrar_cliente_orden/{{object.id}}' data-toggle='modal' data-target='#staticBackdrop'>Confirmar Compra</a>");
        }
    });
})
/* function conpras(){
  $.ajax({
        type:'get',
        url:'registrar_cliente_orden/' + '{{object.id}}',
        success:function(resp){
          $(".modal-title").html(title)
            $(".modal-body").html(resp);
        }
    });
} */
function venta_cliente(){
  var productos="";
  $.ajax({
        type:'get',
        url:'realizar_pedidos/' + '{{object.id}}',
        success:function(resp){
          var total_gasto = 0;
          //console.log(resp.compras);
          for (var i = 0 in resp.compras) {
            productos = productos + " *Producto:* \n";
            productos = productos + resp.compras[i].nombre+"\n Cantidad:";
            productos = productos + resp.compras[i].cantidad+"\n "+" Precio Uni:";
            productos = productos + resp.compras[i].precio_uni+"\n"+" Costo:";
            productos = productos + resp.compras[i].total+"\n";

            total_gasto = total_gasto + parseFloat(resp.compras[i].total);
          }
          var ruta = "https://api.whatsapp.com/send?phone=591"+resp.celular_negocio+"&text="+productos+" \n "+ " *TOTAL A PAGAR: Bs.* "+ total_gasto;
          window.open(ruta, "Diseño Web", "width=600, height=400");
        }
        
    });
  
}


jQuery('<div class="quantity-nav"><div class="quantity-button quantity-up">+</div><div class="quantity-button quantity-down">-</div></div>').insertAfter('.quantity input');
jQuery('.quantity').each(function() {
var spinner = jQuery(this),
input = spinner.find('input[type="number"]'),
btnUp = spinner.find('.quantity-up'),
btnDown = spinner.find('.quantity-down'),
min = input.attr('min'),
max = input.attr('max');

btnUp.click(function() {
var oldValue = parseFloat(input.val());
if (oldValue >= max) {
  var newVal = oldValue;
} else {
  var newVal = oldValue + 1;
}
spinner.find("input").val(newVal);
spinner.find("input").trigger("change");
});

btnDown.click(function() {
var oldValue = parseFloat(input.val());
if (oldValue <= min) {
  var newVal = oldValue;
} else {
  var newVal = oldValue - 1;
}
spinner.find("input").val(newVal);
spinner.find("input").trigger("change");
});

});