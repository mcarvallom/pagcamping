$(document).ready(function(){

    $("#boton1").click(function(){
        var nombre = $("#nombren").val();
        var correo = $("#correon").val();
        var dominio = $("#dominion").val();
        var mensaje = $("#mensajen").val();

        console.log(nombre)

        if(nombre === "" || correo === "" || dominio === ""|| mensaje === ""){
            alert("Todos los campos son obligatorios.");
        }
        else {
            alert("Mensaje enviado con éxito.")
        }

    });
})

