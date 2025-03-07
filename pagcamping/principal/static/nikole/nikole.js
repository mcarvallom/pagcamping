function validar_arriendo() {
    var nombre = document.getElementById("inputName").value;
    var apellido = document.getElementById("inputApellido").value;
    var correo = document.getElementById("inputEmail4").value;
    var celular = parseInt(document.getElementById("inputCelular").value);
    var hastaCuatro = parseInt(document.getElementById("inputCarpaHastaCuatro").value);
    var sobreCuatro = parseInt(document.getElementById("inputSobreCuatro").value);
    var fechaInicio = document.getElementById("inicioFecha").value;
    var fechaFin = document.getElementById("finFecha").value;


    if (nombre === "" || apellido === "" ||correo === "" || isNaN(celular) || isNaN(hastaCuatro) || isNaN(sobreCuatro)|| fechaInicio === "" || fechaFin === "") {
        alert("Todos los campos deben estar llenados");
       
    } else if (hastaCuatro < 0 || hastaCuatro > 10) {
        alert("Debe ingresar un número válido (0 a 10. El máximo de arriendo es de 10 carpas por tipo)");
        
    } else if (sobreCuatro < 0 || sobreCuatro > 10){
        alert("Debe ingresar un número válido (0 a 10). El máximo de arriendo es de 10 carpas por tipo");
        
    } else if (celular < 100000000 || celular > 999999999) {
        alert("Debe ingresar un número de celular válido");

    } else if (fechaInicio >= fechaFin) {
        alert("La fecha de inicio debe ser anterior a la fecha de término");

    } else {
        alert("Se ha arrendado correctamente");
    }    

}

function limpiar_formulario(){

        document.getElementById("formArriendo").reset();

}


//api perfil, cambio imagen
const apiKey = '1hL6Rcu5Q7kVyHIlauxyHZprRIuamE25sgH6uRIWCO7tLI6rup6CcpXU'; // Reemplaza 'Tu-Clave-de-API' con tu clave de API

const gallery = document.getElementById('gallery');

const randomPage = Math.floor(Math.random() * 10) + 1;

fetch(`https://api.pexels.com/v1/search?query=people&page=${randomPage}&per_page=1`, {
    headers: {
        Authorization: apiKey
    }
})
.then(response => response.json())
.then(data => {
    // Procesar los datos recibidos
    data.photos.forEach(photo => {
        const image = document.createElement('img');
        image.src = photo.src.large;
        gallery.appendChild(image);
    });
})
.catch(error => console.log(error));

function modificarPerfil() {
    var nombreMod = document.getElementById("inputNombreEditar").value;
    var correoMod = document.getElementById("inputCorreoEditar").value;
    var celularMod = parseInt(document.getElementById("inputNumeroCelularEditar").value);

    if (nombreMod === "" || correoMod === "" || isNaN(celularMod)) {
        alert("Todos los campos deben estar llenados");
        return false; 
    } else if (celularMod < 100000000 || celularMod > 999999999) {
        alert("Debe ingresar un número de celular válido");
        return false; 
    } else {
        alert("Se ha modificado correctamente");
        return true; 
    }   

   
}





