$(document).ready(function(){

	$("#form_user").css("display", "none");
	$("#add").css("display", "block");




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





	$('#add').click(function(){
		$("#form_user").css("display", "block");
		$("#add").css("display", "none");
  	});

   
	$('#agregar_user').on("click",function(event){
   		event.preventDefault();

   var nombre = $('#nombre').val();
   var departamento = $('#departamento').val();
   var email = $('#email').val();
   var fuera_convenio = $('#fuera_convenio').val();
   
	$.ajax({
		type: 'POST',
		url: '/usuarios/nuevo',
		dataType: 'json',
		data: { 'nombre': nombre, 'departamento': departamento, 'email': email, 'fuera_convenio': fuera_convenio},
		success: function(data){
   			//alert(data.mensaje);
   			$('#lista_users').load('/usuarios/listar');
		}
   		});
   	});
	
});



//	$.post("/usuarios/nuevo", { 'nombre': nombre, 'departamento': departamento, 'email': email, 'fuera_convenio': fuera_convenio})
 //  		.done(function(data){
 //  			alert(data.mensaje);
			
			//$.ajax({
			//	url: "usuarios/listar",
			//	success: function(data) {
        	//	$('#lista_users').html(data);
          	//	}
    		//});
   		
   	



//   $.ajax({
//   	type: 'POST',
//    url: '/usuarios/nuevo',
 //   dataType: 'json',
//    data: { 'nombre': nombre, 'departamento': departamento, 'email': email, 'fuera_convenio': fuera_convenio},
//	success: function(data){
//   		alert("Usuario añadido!");
 //   	};

  

//   $.post("/personas/nuevo", { nombre: nombre, departamento: departamento, email: email, fuera_convenio: fuera_convenio})
//   		.done(function(data){
//   			alert(data.mensaje);
//   		});


//function comprobar()
//{
//   var nombre = document.add_persona.nombre_apellido.value;
//   var departamento = document.add_persona.departamento.value;
//
//   if (nombre_apellido.length > 30)
//   {
//      alert("Tu nombre es demasiado grande. Redúcelo.");
//      return false;
//   }
//   
//   if (departamento.lenght > 40)
//   {
//      alert("El nombre de Dpto. es demasiado grande. Redúcelo");
//      return false;
//   }
//   
//   return true;
//}
