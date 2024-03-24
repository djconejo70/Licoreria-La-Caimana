
// const articulo = async () => {
//     try {
//         const response = await fetch("agregar");
//         const users = await response.json();
//         console.log(data);
//     } catch (ex) {
//         alert(ex);
//     }
// };

// window.addEventListener("load", async () => {
//     await articulo();
// });

// var venta={
//     items:{
//         cliente: '',
//         fecha_compra: '',
//         total: 0.00,
//         productos: []
//     },
//     add:function(item){
//         alert('paso add');
//         this.items.productos.push(item);
//         this.list();
//     },

//     list: function() {
//         $('#tblProductos').DataTable({
//             responsive:true,
//             autoWidth:false,
//             destroy:true,
//             deferRender:true,
//             data:this.items.productos,
//             columns:[
//                 {"data":"codigo_articulo"},
//                 {"data": "nombre"},
//             ],
//             initComplete: function(settings,json){

//             }
//         });
// },
// };

// $(document).ready(function(){
//     $('#form_dt').submit(function(e){
//         // e.preventDefault();

//         $.ajax({
//             url:$(this).attr('action'),
//             type: $(this).attr('method'),
//             data: $(this).serialize(),
//             success: function(json){
//                 alert('paso aqui')
//                 // console.log(json)
//                 venta.items.productos.push(ui.item)
//                 console.log(venta.items)                    
//             }
//         })
                
//         console.log(e);
//     })    
//   })

// function miFunc(){
//     var x = document.getElementById("codigo_articulo").value
//     alert(x)
//     $.ajax({
//         url:$(this).attr('action'),
//         type: $(this).attr('method'),
//         data: $(this).serialize(),
//         success: function(json){
//             alert('paso aqui', x)
//             // console.log(json)
//             venta.items.productos.push(ui.item)
//             console.log(venta.items)
//             alert('paso aqui 2')             
//         }
//     })
//   }
