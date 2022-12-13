// somehow know all current markers, they need tags on them

// there's a dropdown, which user can select a tag from

// once a tag is selected, remove all markers that do not have the associated tag
/* THE PLAN
get filterOption from user

if list[i].tag != filterOption
    remove()

filterOption == defaultFilter
for i in list
    if list[i] not in map,
        addTo(map)
*/

// alert("this is a message")

function mapFilter(dropdown)
{
    // get filter option from html dropdown
    var selectedText = dropdown.options[dropdown.selectedIndex].innerHTML;

    // remove markers
    for (let i = 0; i < markers.length; i++)
    {
        if (selectedText == "None")
        {
            markers[i].marker.addTo(map);
        }
        else if (markers[i].tag != selectedText)
        {
            markers[i].marker.remove();
        }
        else
        {
            markers[i].marker.addTo(map);
        }
    }
    
    // redraw map
	osm.redraw();
}
