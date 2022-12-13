function toggleSidebar() {
    currentWidth = document.getElementById("sb").style.width;
    if (currentWidth == "0px")
    {
        document.getElementById("sb").style.width = "350px";
        document.getElementById("map").style.marginLeft = "350px";
        // show buttons
        document.getElementById("buttons").style.display = "block";
    }
    else 
    {
        document.getElementById("sb").style.width = "0";
        document.getElementById("map").style.marginLeft = "0";
        // hide buttons
        document.getElementById("buttons").style.display = "none";
    }
    map.invalidateSize(); // resize map because its container size changed and this avoids an ugly grey bar from showing up in the "new" space
}
