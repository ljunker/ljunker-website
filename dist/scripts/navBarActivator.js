function navBarActivate() {
    var currentPath = window.location.href;

    // Get the element with id "nav"
    var navElement = document.getElementById("nav");

    if (navElement) {
    // Get all <a> elements inside the "nav" element
        var links = navElement.getElementsByTagName("a");

        // Loop through each <a> element
        for (var i = 0; i < links.length; i++) {
            // Check if the href attribute matches the current URL
            if (links[i].href === currentPath) {
                // Add the "active" class to the matching <a> element
                links[i].className += " active";
            }
            if (currentPath.endsWith("/") && links[i].href.endsWith("index.html")) {
                links[i].className += " active";
            }
        }
    }
}