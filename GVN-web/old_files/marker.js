

//Markers popups
//latlng = [39.0804287148205, -108.56063938716765];
//var popup = L.popup(latlng, { content: '<p>Hello world!<br />This is a nice popup.</p>' }).openOn(map);
//~~or~~
function markerStruct(tag, long, lat, popupText)
{
    this.tag = tag;
    this.marker = L.marker([long, lat], { icon: greenIcon })
    this.popupText = popupText;
}
// this isnt properly organized yet since im just playing around w/ making markers appear/dissappear so everything is pretty hardcoded and static atm
// planning to make an array to store all the information once i have access to the database and/or test data
// filter function will just iterate over the array in the future
// use array.push(new markerStruct(tag, long, lat, popupText)) to add new entries
// all events will need to be tagged when read in
var markers = []

var greenIcon = new L.Icon({
    iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
});

maverickCenter = new markerStruct(
    "Food",
    39.0829654151576, 
    -108.55489457460875,
    "Maverick Center"
);
maverickCenter.marker.addTo(map).bindPopup(maverickCenter.popupText);

cmu = new markerStruct(
    "Music",
    39.08081568048276, 
    -108.55380362502599,
    "Student Center"
);
cmu.marker.addTo(map).bindPopup(cmu.popupText);

confluence = new markerStruct(
    "Sports",
    39.08074188134892, 
    -108.56024045469952,
    "Confluence Hall"
);
confluence.marker.addTo(map).bindPopup(confluence.popupText);

markers.push(maverickCenter);
markers.push(cmu);
markers.push(confluence);
