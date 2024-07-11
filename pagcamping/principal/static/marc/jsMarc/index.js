  function initMap() {
    var ubicacion = {lat: -33.04122688, lng: -71.50145};
  
    var opcionesMapa = {
      center: ubicacion,
      zoom: 17 
    };
  
    // Crear un nuevo mapa en el elemento con id 'map'
    var mapa = new google.maps.Map(document.getElementById('map'), opcionesMapa);
  
    // Crear un marcador en la ubicación especificada
    var marcador = new google.maps.Marker({
      position: ubicacion,
      map: mapa,
      title: '' 
    });
  }
  // script.js

  document.addEventListener('DOMContentLoaded', (event) => {
    const button = document.getElementById('subscribeButton');
    const modal = document.getElementById('myModal');
    const successMessageElement = document.getElementById('successMessage');
    const span = document.getElementsByClassName('close')[0];

    // Recuperar el estado del botón de localStorage si está disponible
    const buttonText = localStorage.getItem('buttonText') || 'Subscribir';
    button.textContent = buttonText;

    button.addEventListener('click', () => {
        if (button.textContent === 'Subscribir') {
            button.textContent = 'Darse de baja';
            successMessageElement.textContent = 'Se ha suscrito con éxito';
        } else {
            button.textContent = 'Subscribir';
            successMessageElement.textContent = 'Se ha dado de baja con éxito';
        }
        localStorage.setItem('buttonText', button.textContent);

        // Mostrar la ventana emergente
        modal.style.display = 'block';

        // Ocultar la ventana emergente después de 3 segundos
        setTimeout(() => {
            modal.style.display = 'none';
        }, 3000);
    });

    // Cerrar la ventana emergente cuando se hace clic en el botón de cerrar
    span.addEventListener('click', () => {
        modal.style.display = 'none';
    });

    // Cerrar la ventana emergente cuando se hace clic fuera de ella
    window.addEventListener('click', (event) => {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    });
});


  
  
