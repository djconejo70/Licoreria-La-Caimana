  $(document).ready(function () {
    const $FormularioEditar=document.getElementById('formulario_editar');
    const $Articulo=document.getElementById('articulo_editar');
    const $TipoUnidad=document.getElementById('tipo_unidad_editar');
    
    (function() {
    
    $FormularioEditar.addEventListener('submit', function(e) {
      let nombre = String($Articulo.value).trim();
      let unidad = String($TipoUnidad.value).trim();
    
      if (nombre === "" || nombre === null || nombre.length === 0)  {
        alert ('ARTICULO no puede estar vacio');
        e.preventDefault();
      } 
      if (unidad === "" || unidad === null || unidad.length === 0)  {
        alert ('PRESENTACION no puede estar vacio');
        e.preventDefault();
      } 
    } );
    
    
    } )();
    } );
    
    