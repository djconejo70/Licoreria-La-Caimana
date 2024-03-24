


$(document).ready(function () {
  const $FormularioEditar=document.getElementById('formulario_editar');
  const $Articulo=document.getElementById('articulo_editar');
  const $TipoUnidad=document.getElementById('tipo_unidad_editar');
  
  (function() {
    
  
  $FormularioEditar.addEventListener('submit', function(e) {
    let nombre = String($Articulo.value).trim();
    let unidad = String($TipoUnidad.value).trim();
  
    if (nombre === "" || nombre === null || nombre.length === 0)  {
      Swal.fire(
        'Tarea no se puede realizar',
        'ARTICULO no puede estar vacio...!',
        'warning'
      )
      e.preventDefault();
    } 
    if (unidad === "" || unidad === null || unidad.length === 0)  {
      Swal.fire(
        'Tarea no se puede realizar',
        'PRESENTACION no puede estar vacio...!',
        'warning'
      )
      e.preventDefault();
    } 
  } );
  
  
  } );
  } );
  

$(document).ready(function () {
const $FormularioAñadir=document.getElementById('formulario_añadir');
const $Articulo=document.getElementById('articulo');
const $TipoUnidad=document.getElementById('tipo_unidad');

(function() {

$FormularioAñadir.addEventListener('submit', function(e) {
  let nombre = String($Articulo.value).trim();
  let unidad = String($TipoUnidad.value).trim();

  if (nombre === "" || nombre === null || nombre.length === 0)  {
    Swal.fire(
      'Tarea no se puede realizar',
      'ARTICULO no puede estar vacio...!',
      'warning'
    )
    e.preventDefault();
  } 
  if (unidad === "" || unidad === null || unidad.length === 0)  {
    Swal.fire(
      'Tarea no se puede realizar',
      'PRESENTACION no puede estar vacio...!',
      'warning'
    )
    e.preventDefault();
  } 
} );

} )();


} );

$(document).ready(function () {

  const btnEliminacion = document.querySelectorAll(".btnEliminacion");

  btnEliminacion.forEach(btn => {
      btn.addEventListener('click', (e) => {
          const confirmacion = confirm('¿Seguro de eliminar este articulo?');
          if (!confirmacion) {
              e.preventDefault();
          }
      });
  });
  
});


$(document).ready(function() {
    $('#tabla_inventario').DataTable( {
        "language": {
            url : 'static/licoreriaapp/datatable/spanish.txt' 
          },
        dom: 'Bfrtip',
        dom: "<'row'<'col-sm-4'li><'col-sm-4 text-center'B><'col-sm-4'f>>" +
                "<'row'<'col-sm-12'tr>>" +
                "<'row'<'col-sm-5'i><'col-sm-7'p>>",
        buttons: [{
            //Botón para Excel
            extend: 'excel',
            footer: true,
            title: 'Archivo',
            filename: 'Export_File',
            className: 'btn btn-info btn-sm',
    
            //Aquí es donde generas el botón personalizado
            text: '<button style= "border: none; padding: 0; background-color: transparent; color:#FCFCFC">Excel <i class="fas fa-file-excel"></i></button>'
          }, 
          //Botón para PDF
          {
            extend: 'pdf',
            footer: true,
            title: 'Archivo PDF',
            filename: 'Export_File_pdf',
            className: 'btn btn-primary btn-sm',
            text: '<button style= "border: none; padding: 0; background-color: transparent; color:#FCFCFC" >PDF<i class="fas fa-file-pdf"></i></button>'
            
          },

        //Botón para print
        {
            extend: 'print',
            footer: true,
            filename: 'Export_File_print',
            className: 'btn btn-warning btn-sm',
            text: '<button style= "border: none; padding: 0; background-color: transparent; color:#FCFCFC" >Print<i class="fas fa-file-print"></i></span>'
        },
        ]
        
        
    } );
} );












