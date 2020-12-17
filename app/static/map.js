export class Map {
  constructor() {
    this.place = {};
    this.zoom = 7;
  }

  initMap(longitude, latitude, mapId) {
    this.place = {
      lat: latitude,
      long: longitude,
    };

    // Get a map
    const map = L.map(mapId).setView(
      [this.place.lat, this.place.long],
      this.zoom
    );

    // Get a tile (images)
    const mainLayer = L.tileLayer(
      "https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}",
      {
        attribution:
          'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: "mapbox/streets-v11",
        tileSize: 512,
        zoomOffset: -1,
        accessToken:
          "pk.eyJ1IjoibGFtaWE3IiwiYSI6ImNraWl0bG50ejBjemMyc3FwNXpmYjN3ZGEifQ.1-8RIk4lLjGMJLcpWZ4Vyw",
      }
    );

    // Add tile to map
    mainLayer.addTo(map);

    // Add marker
    const marker = L.marker([this.place.lat, this.place.long]).addTo(map);
  }
}
