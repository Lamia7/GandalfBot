function init() {
    console.log('Started map');

    const place = {
        lat: 48.114384,
        long: -1.669494,
    }
    const zoom = 7;

    // Get a map
    const map = L.map('map').setView([place.lat, place.long], zoom);
    // (objet L mis à dispo grâce au scripte leaflet), le tout ns retourne un objet map

    // Get a tile (images)
    const mainLayer = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox/streets-v11',
        tileSize: 512,
        zoomOffset: -1,
        accessToken: 'pk.eyJ1IjoibGFtaWE3IiwiYSI6ImNraHA3YjR0MjB1MGwydms2Mm55bWxlbW0ifQ.zMlnj664_c4_ZNFCCoaBXA'
    });

    // Add tile to map
    mainLayer.addTo(map);

    // Add marker
    const marker = L.marker([place.lat, place.long]).addTo(map)
}

//init()