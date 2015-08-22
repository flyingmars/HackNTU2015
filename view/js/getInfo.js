//to get info from http://temp1.mar98.tk/HackNTU2015/forecast.php
// input are probability and intensity
$.getJSON("http://temp1.mar98.tk/HackNTU2015/forecast.php", function(data) {
    var items = [];
    $.each(data, function(key, val) {
        items.push("<p> The " + key + " of rain is " + val + ".</p>");
    });

    $("#show").append(items.join(""));

    /*$("<ul/>", {
        "class": "my-new-list",
        html: items.join("")
    }).appendTo("#show");*/
});