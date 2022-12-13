//Layers-----------------vvv  

// Of the different maps below, the one on the bottom is the one
// that will be displayed on the website. Either comment out the other 
// ones or move the one you want to the bottom for now.

//https://leaflet-extras.github.io/leaflet-providers/preview/  -  More layers here
//Open Street Map
var osm = L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
});
//Google streets
var googleStreets = L.tileLayer('http://{s}.google.com/vt/lyrs=m&x={x}&y={y}&z={z}', {
    maxZoom: 20,
    subdomains: ['mt0', 'mt1', 'mt2', 'mt3']
});
//Google Sat
var googleSat = L.tileLayer('http://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
    maxZoom: 20,
    subdomains: ['mt0', 'mt1', 'mt2', 'mt3']
});
//End of layers--------------^^^

//Layer selector---vvv

// Should display a selection box on the top rigt of the map
// that allows you so select different map layers like satelite, topo, OSM...

var baseMaps = {
    "OpenStreetMap": osm,
    //"Mapbox Streets": streets,
    "Google Streets": googleStreets,
    "Google Satelite": googleSat
};
var overlayMaps = {
   // "Buildings": buildings
   //"Markers": markers
};

var layerControl = new L.control.layers(baseMaps, overlayMaps);
osm.addTo(map);
map.addControl(layerControl);
// var baseMaps = {
//     "<span style='color: gray'>Grayscale</span>": grayscale,
//     "Streets": streets
// };
//End of Map selector ---^^^