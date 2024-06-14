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
  const buttonText = localStorage.getItem('buttonText') || 'Subscribir';
  button.textContent = buttonText;

  button.addEventListener('click', () => {
      if (button.textContent === 'Subscribir') {
          button.textContent = 'Darse de baja';
      } else {
          button.textContent = 'Subscribir';
      }
      localStorage.setItem('buttonText', button.textContent);
  });
});

