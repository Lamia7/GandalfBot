
export function initMap (longitude, latitude) {
    const place = {
        lat: latitude,
        long: longitude,
    }
    const zoom = 7;

    // Get a map
    const map = L.map('map').setView([place.lat, place.long], zoom);

    // Get a tile (images)
    const mainLayer = L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox/streets-v11',
        tileSize: 512,
        zoomOffset: -1,
        accessToken: "pk.eyJ1IjoibGFtaWE3IiwiYSI6ImNraWFvYmp5dzA0dHIyeWswa3lxbXQyODYifQ.a7-70MrQHZZOU2lKseHL4g"
    });

    // Add tile to map
    mainLayer.addTo(map);

    // Add marker
    const marker = L.marker([place.lat, place.long]).addTo(map)
}
