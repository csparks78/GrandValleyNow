
var geoLocations = { "type": "FeatureCollection", "features": 
[
{ "type": "Feature", "properties": {}, "geometry": { "type": "Point", "coordinates": [-108.55448126792908, 39.08308891281086] } },
{ "type": "Feature", "properties": {}, "geometry": { "type": "Point", "coordinates": [-108.55553269386292, 39.08208953715821] } }, 
{ "type": "Feature", "properties": {}, "geometry": { "type": "Point", "coordinates": [-108.55411648750305, 39.07889976849927] } }, 
{ "type": "Feature", "properties": {}, "geometry": { "type": "Point", "coordinates": [-108.55308651924133, 39.08054047691818] } }, 
{ "type": "Feature", "properties": {}, "geometry": { "type": "Point", "coordinates": [-108.55361223220825, 39.07781704661579] } }, 
{ "type": "Feature", "properties": {}, "geometry": { "type": "Point", "coordinates": [-108.56004953384400, 39.08062376059192] } }
] 
}

L.geoJSON(geoLocations).addTo(map)