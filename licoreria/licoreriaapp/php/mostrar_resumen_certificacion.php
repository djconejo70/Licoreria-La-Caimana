<?php 
session_start();
header('Content-Type: text/html; charset=UTF-8');
include("../../conf/config.php"); 
include("../../librerias/funciones.php");
include("../../librerias/noCache.php");
$id_usuario = $_SESSION['DATOS_USUARIO_SIGMAESTRATH']['usuario'];
controlSesion($id_usuario);
$border=0;
$filas = 0;
 
?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<link rel="stylesheet" type="text/css" href="../../css/estilos.css" >
	<link rel="stylesheet" type="text/css" href="../../css/tabla_gestion.css" >
	<script src="../../../js/jquery.js" type="text/javascript"></script>
	<script src="../../../js/jquery.alerts.js" type="text/javascript"></script>
    <script src="../../js/jquery.dataTables.js" type="text/javascript" ></script>
    <script src="../../js/adicional_dataTables.js" type="text/javascript" ></script>
	<script src="../../js/funciones_javascript.js" type="text/javascript"></script>  
	<script type="text/javascript">
		function mostrar(){
            $("#opc_gerencia").attr("disabled", true);
            var alto = $(window).height();
            var max_filas = 22;
            if (alto > 700)
                 max_filas = 25;
			var usuario = '<?php echo $id_usuario ?>';
			$.ajax({
				beforeSend: function(){
					$('#td_wait').html('<IMG title="Cargando..." id= "img_cargando" name="img_cargando" alt="Cargando..." src="../../../imagenes/img_load.gif" />');
				},
				cache: false,
				type: "POST",
				url: 'consulta_resumen_certificacion.php',
				success: function(datos){
					$("#tabla").html(datos);
                    if( $("#tbl_consuta tr").length > 3){
                        
                        $("#tbl_consuta").dataTable({
                            "iDisplayLength": max_filas,
                            "bFilter": true,
                            "sPaginationType": "four_button",
                            "bSort": false
                        });
                        $('#td_wait').html('<a href="consulta_resumen_certificacion_pdf.php" target="_blank" title="Exportar a formato .PDF"><IMG id="img_export_pdf" name="img_export_pdf" src="../../../imagenes/exportar_a_pdf.png" alt=".PDF" width="25" height="25" align="left" border="0" /></a>');
                    }
                    else
                        $('#td_wait').html('&nbsp;');
				}
			});
			return false;
		}

        function init(){
            doResize(29);
            mostrar();
            return 0;
        }
	</script>
</head>
<body topmargin="5px;" width="1070px" onResize="doResize(29);" onload="init();">
	<table id="tbl_reporte" align="center" border="<?php echo $border ?>" cellpadding="0" cellspacing="0" width="100%" height="100%" style="border-style:solid;border-left-width:1px;">
		<TR>
			<TD style="width:100%;">
				<div id="div_header" align="center" style="overflow:hidden;width:100%;">
					<table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" height="100%" >
						<TR>
							<TD nowrap class="tituloModulo" width="10px" style="text-align:center">
								<IMG src="../../../imagenes/img_separador.png" width="3" height="23" align="middle" border="0">	
							</TD>
							<TD nowrap class="tituloModulo" width="360px" >
								&nbsp;Reporte Resumen Certificación de Trabajadores
							</TD>
							<TD nowrap class="tituloModulo">
								&nbsp;
							</TD> 
 							<TD nowrap class="tituloModulo"  style="text-align:center;height:25px;width:18px">
								<IMG src="../../../imagenes/img_separador.png" width="3" height="23" align="middle" border="0">
							</TD>                                                         
							<TD id="td_wait" nowrap class="tituloModulo" width="35px">
								&nbsp;
							</TD>
						</TR>
					</table>
				</div>
			</TD>
		</TR>
		<TR id="tr_reporte" valign="top">
			<TD id="td_reporte" nowrap align="left" style="height:100%;" >
				<div id="div_reporte" align="center" onscroll="keepScroll('div_header',this)" style="overflow-x:auto;overflow-y:auto;width:100%;height:100%;">	
					<div id="tabla" ></div>
				</div>
			</TD>
		</TR>
	</table> 
</body>
</html>

