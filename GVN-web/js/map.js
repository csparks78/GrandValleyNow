//------------------------------------------------------//
//               MAP INITIALIZATION                     //
//------------------------------------------------------//

var map = L.map('map').setView([39.080065, -108.554671], 14);
//map.locate({setView: true, maxZoom: 16});    //Enable this line in production to allow a popup
//that asks for the users location


//------------------------------------------------------//
//                      LAYERS                          //
//------------------------------------------------------// 

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

//------------------------------------------------------//
//               LAYER SELECTOR                         //
//------------------------------------------------------//

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
//End of Map selector ------------------------------------------



//Markers popups
//latlng = [39.0804287148205, -108.56063938716765];
//var popup = L.popup(latlng, { content: '<p>Hello world!<br />This is a nice popup.</p>' }).openOn(map);
//~~or~~
//------------------------------------------------------//
//                      ICONS                           //
//------------------------------------------------------//
var greenIcon = new L.Icon({
    iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
});
var redIcon = new L.Icon({
    iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
});
var customIcon = new L.icon({
    iconUrl: 'https://leafletjs.com/examples/custom-icons/leaf-green.png',
    iconSize: [38, 40], // size of the icon
    iconAnchor: [10, 40], // point of the icon which will correspond to marker's location
    popupAnchor: [5, -40] // point from which the popup should open relative to the iconAnchor
});

//------------------------------------------------------//
//           HARD CODED MARKERS                         //
//------------------------------------------------------//

// var name = "Maverick center"
// var name2 = "Robinson Theater"
// cmu = L.marker([39.08081568048276, -108.55380362502599]).addTo(map)
//     .bindPopup('CMU');
//     //.openPopup();
// confluence = L.marker([39.08074188134892, -108.56024045469952]).addTo(map)
//     .bindPopup('Confluence');
//     //.openPopup();
// houston = L.marker([39.07796145648452, -108.55352431079919]).addTo(map)
//     .bindPopup('Houston');
//     //.openPopup();
// robinsonTheater = L.marker([39.07906815468065, -108.55289782121902]).addTo(map)
//     .bindPopup(name2);
//     //.openPopup();
// maverickCenter = L.marker([39.0829654151576, -108.55489457460875], { icon: greenIcon }).addTo(map)
//     .bindPopup(name);
//.openPopup();

// End of hard coded markers--------------------------------------------

//------------------------------------------------------//
//         DISPLAY RESULTS FROM SCRAPER                 //
//------------------------------------------------------//

$.getJSON("scraper/data/dataPresence.json", function (json1) {
    
    var who = "<u>Who</u>: ";
    var what = "<u>What</u>: ";
    var where = "<u>Where</u>: ";
    var when  = "<u>When</u>: ";
    var time = "<u>Time</u>: ";

    for (var i = 0; i < json1.length; i++) {
        var place = json1[i];
        // Creating a marker and putting it on the map
        console.log(json1.length)
        var marker = L.marker(place.coordinates, { icon: greenIcon });
        marker.addTo(map).bindPopup(who + place.organization + '</br>' 
                                    + what + place.title + '</br>' + where + place.loc + '</br>' 
                                    + when + place.date + '</br>' + time + place.stime + '</br>' );
    }
});

$.getJSON("scraper/GJSentinel-Scraper/grandjunction_events.json", function (json2) {

    var tag = "<u>Type of Event</u>:  ";
    var title = "<u>What</u>: ";
    var address = "<u>Address</u>: ";
    var when  = "<u>When</u>: ";
    var location = "<u>Location</u>: ";
    var start_time = "<u>Time</u>: ";    

    for (var i = 0; i < json2.length; i++) {
        var place2 = json2[i];
        //Creating a marker and putting it on the map
        var add = place2.link;
        var marker = L.marker(place2.coordinates, { icon: redIcon });
        marker.addTo(map).bindPopup(tag + place2.tag + '</br>' + title + place2.title 
                                    + '</br>' + location + place2.location_in_words + '</br>' + address 
                                    + place2.address + '</br>' + when + place2.month_or_today + "/" 
                                    + place2.day_of_month + '</br>' + start_time + place2.start_time 
                                    + '</br>' + '<a href="' + add + '">Link to website</a>');
    }

});
