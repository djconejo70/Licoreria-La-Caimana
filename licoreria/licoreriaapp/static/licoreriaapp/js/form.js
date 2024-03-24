
 var venta = {
   items: {
     fecha: '',
     cliente: '',
     ci_rif: '',
     total: 0.00,
     productos: []
    },
    list:function(){
      $('#data').Datatable( {
        resposive: true,
        autoWidth: false,
        destroy: true,
        data: this.items.productos,
        columns: [
          {"data": "id"},
          {"data": "codigo_articulo"},
          {"data": "precio_sugerido_venta"},
          {"data": "cantidad"},
          {"data": "cantidad_venta"},
          {"data": "subtotal"},


        ],
        columnDefs:[
          {
            targets: [2],
            class: 'text-center',
            orderable: false,
            render: function (data, type, row) {
                return '$'+parseFloat(data).toFixed(2);
            }
          },

          {
            targets: [5],
            class: 'text-center',
            orderable: false,
            render: function (data, type, row) {
                return '$'+parseFloat(data).toFixed(2);
            }
          },
          {
            targets: [0],
            class: 'text-center',
            orderable: false,
            render: function (data, type, row) {               
            return '<a rel="remove" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';                
            }
          }

        ],
        initComplete: function(settings, json){

        }
       }

      )
    
    }
  };

// $(function () {
//   $('.select2').select2({
//       theme: "bootstrap4",
//       language: 'es'
//   });
// });


// $('input[name="search"]').autocomplete({
//   source: function (request, response) {
//       $.ajax({
//           url: window.location.pathname,
//           type: 'POST',
//           data: {
//               'action': 'search_articulos',
//               'term': request.term
//           },
//           dataType: 'json',
//       }).done(function (data) {
//           response(data);
//       }).fail(function (jqXHR, textStatus, errorThrown) {
//           //alert(textStatus + ': ' + errorThrown);
//       }).always(function (data) {

//       });
//   },
//   delay: 500,
//   minLength: 1,
//   select: function (event, ui) {
//       console.log(ui.item);
//   }
// });

// $(function () {
//   $("#sideBarToggle").click();
//   $("#articulo").select2({
//       placeholder:"Seleccione Cliente",
//       allowClear:true
      
//   });
// });


