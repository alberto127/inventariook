

function abrir_modal(){
  $('#form_user').dialog({
    autoOpen:false,
    modal:true,
    title:'Ingreso de usuario',
    width:300,
    height:'auto',
    });
  };
    

    $('#add').click(function(){
      $("#form_user").dialog('open');
      });


//function cerrar_modal()
//{
//    modal.dialog("close");
//}



   $('#agregar_user').click(function(){


   var nombre = $('#nombre').val();
   var departamento = $('#departamento').val();
   var email = $('#email').val();
   var fuera_convenio = $('#fuera_convenio').val();
   

  $.post("/usuarios/nuevo", { 'nombre': nombre, 'departamento': departamento, 'email': email, 'fuera_convenio': fuera_convenio})
      .done(function(data){
        alert(data.mensaje);
      });

// $(function(){
// 	$('#form_user').dialog({
// 		autoOpen:false,
// 		modal:true,
// 		title:'Ingreso de usuario',
// 		width:300,
// 		height:'auto',
// 	});
// 	$('#add').click(function(){
// 		$("#form_user").dialog('open');
// 	});
// });


