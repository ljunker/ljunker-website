function findGetParameter(parameterName) {
    var result = null,
        tmp = [];
    location.search
        .substr(1)
        .split("&")
        .forEach(function (item) {
          tmp = item.split("=");
          if (tmp[0] === parameterName) result = decodeURIComponent(tmp[1]);
        });
    return result;
}

function loadArticle() {
    var z, i, elmnt, file, xhttp;
    /* Loop through a collection of all HTML elements: */
    z = document.getElementsByTagName("*");
    for (i = 0; i < z.length; i++) {
      elmnt = z[i];
      /*search for elements with a certain atrribute:*/
      file = elmnt.getAttribute("load-article");
      if (file) {
        file = findGetParameter("article");
          file = "article/" + file + ".md";
        /* Make an HTTP request using the attribute value as the file name: */
        elmnt.setAttribute("src", file);
        elmnt.removeAttribute("load-article");
        return;
      }
    }
  }