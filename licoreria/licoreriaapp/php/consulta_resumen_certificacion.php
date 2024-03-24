<?php 
session_start();
header('Content-Type: text/html; charset=UTF-8');
include("../../conf/config.php"); 
include("../../librerias/funciones.php");
include("../../librerias/noCache.php");


$Cnn = conectarse();
$filas = 0;
if ($Cnn) { 
	$strSQL = "SELECT * FROM sig_maestra_th.func_con_resumen_certificacion_xgerencia()";
    $rst_tabla = pg_query($Cnn,$strSQL);     
    $filas = pg_num_rows($rst_tabla);
}
?>
		<table style="font-size:12px;font-family: open, Free-sans, DejaVuSans,Verdana,Arial;text-align:center;border-collapse:collapse;width:860px;margin-top:8px" >
			<tr>
				<td>
					<table id="tbl_consuta" name="tbl_consuta" style="width:100%;border-collapse:collapse;" >
					<thead>
						<tr> 
							<td colspan="5" class="Title" style="border: solid 1px #ccc;">RESUMEN DE TRABAJADORES CERTIFICADOS</td>
						</tr>
						<tr>
							<th class="SubTitle" style="width:400px;border: solid 1px #ccc;">GERENCIA</th>
							<th class="SubTitle" style="width:100px;border: solid 1px #ccc;">TOTAL</th>
							<th class="SubTitle" style="width:100px;border: solid 1px #ccc;">CERTIFICADOS</th>
							<th class="SubTitle" style="width:120px;border: solid 1px #ccc;"> NO CERTIFICADOS</th>
							<th class="SubTitle" style="width:100px;border: solid 1px #ccc;">FALTAN</th>                              
						</tr>
					</thead>
					<tbody>
<?php
	if ($filas > 0)
	{
        $i = 0;
		while( $datos = pg_fetch_array($rst_tabla) )
		{	
			$faltante = $datos['cantidad_total'] - ($datos['cantidad_certificada'] + $datos['cantidad_no_certificada']);
			echo '<tr>';
				echo '<td class="Nivel2Valc" style="border: solid 1px #ccc;text-align:left">'.$datos['descripcion'].'</td>'; 
				echo '<td class="Nivel2Valc" style="border: solid 1px #ccc;text-align:right">'.$datos['cantidad_total'].'</td>'; 
                echo '<td class="Nivel2Valc" style="border: solid 1px #ccc;text-align:right">'.$datos['cantidad_certificada'].'</td>';  
                echo '<td class="Nivel2Valc" style="border: solid 1px #ccc;text-align:right">'.$datos['cantidad_no_certificada'].'</td>';                 
                echo '<td class="Nivel2Valc" style="border: solid 1px #ccc;text-align:right">'.$faltante.'</td>';                                                                
			echo '</tr>';
		}
	}
	else{
		echo '<tr style="text-align:center;height:50px">';
			echo '<td colspan="5" style="font-weight:bold;font-size:12px;color:red;border: solid 1px #ccc;">&iexcl; NO EXISTEN REGISTROS !</td>';
		echo '</tr>';
	}
	echo '</tbody>';
echo '</table>';
echo '</td>';
echo '</tr>';
echo '</table>';
if($rst_tabla)
	pg_free_result($rst_tabla);
if($Cnn)
	desconectarse($Cnn);
?>
