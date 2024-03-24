<?php 
session_start();
header('Content-Type: text/html; charset=UTF-8');
include("../../conf/config.php"); 
include("../../librerias/funciones.php");
include("../../librerias/noCache.php");

?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<script src="../../../js/jquery.js" type="text/javascript"></script> 
		<link rel="stylesheet" type="text/css" href="../../css/estilosm.css" >  
	<script type="text/javascript">
	function init(){	
	codigo_articulo = 1;
    var fila=codigo_articulo;
    articulo = 'cerveza';
    presentacion = 'CAJAS 24';
    stock = 100;
    precio = 17;
    cadena='<tr id="' + fila + '">';    
    cadena += '<td><input id="cantidad_' + fila + '" type="number" min="1" max="999999999999" value="1" style="width:50px;heigth:6px"> </input></td>';
    cadena += "<td>" + articulo + "</td>";
    cadena += "<td>" + presentacion + "</td>";
    cadena += "<td>" + stock + "</td>";
    cadena += "<td>" + precio + "</td>";
    cadena +="<td></td>";
    cadena +='<td><IMG src="../static/licoreriaapp/img/plus.png" width="25px" onclick="sumaritems(this)"></td></tr>';

$("#tbl_recepcion_clap >tbody:first").prepend(cadena);

cadena = '<tr id="2"><td><input id="cantidad_2" type="number" min="1" max="999999999999" value="1" style="width:50px;heigth:6px"> </input></td><td>Cerveza Polar </td><td> Caja 36 unidades </td><td> 45 </td><td> 19.00</td><td></td><td><IMG src="../static/licoreriaapp/img/plus.png" width="25px" onclick="sumaritems(this)"></td></tr>';
$("#tbl_recepcion_clap >tbody:first").prepend(cadena);
//sumaritems(this);
}

function sumaritems(fila) {
  var registro = $(fila).closest('tr').attr('id');
  var obj_cantidad = '#cantidad_' + registro;
  alert(obj_cantidad);
  var x = $(obj_cantidad).val();  
  alert(x);
  x=++x;
    $(obj_cantidad).val(x); 
}

	</script>
</head>
<body topmargin="5px;" width="1070px" onload="init();" >
			<table id="tbl_recepcion_clap" cellspacing="0" cellspadding="0" style="margin-top:0px;width:800px;font-size:10px;font-family: sans-serif, DejaVuSans,Verdana,Arial;text-align:center;border-collapse:collapse;margin-top:10px;margin-bottom:20px;">
				<thead id="recepcion_clap">
				<tr>
					<th class="SubTitle" style="width:80px;border: solid 1px #ccc;">CANTIDAD</th>  
					<th class="SubTitle" style="width:300px;border: solid 1px #ccc;">PRODUCTO</th> 
					<th class="SubTitle" style="border: solid 1px #ccc;">PRESENTACION</th>
					<th class="SubTitle" style="border: solid 1px #ccc;">STOCK</th>
					<th class="SubTitle" style="border: solid 1px #ccc;">PRECIO</th>
					<th class="SubTitle" style="width:50px;border: solid 1px #ccc;">SUB TOTAL</th>	
					<th class="SubTitle" style="width:50px;border: solid 1px #ccc;"></th>						
				</thead>
				<tbody id="cuerpo">;
				</tbody>								
				</table>
				</td>
				</tr>
				</table>			
</body>
</html>

