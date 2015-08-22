var input = [];
$("#submit").click(function() {
    input[0] = $('#longitude').val();
    input[1] = $('#latitude').val();
    input[2] = $('#date').val();
    input[3] = $('#time').val();

    $("#show").append("<p>longitude: " + input[0] +
        "<br>latitude: " + input[1] +
        "<br>date: " + input[2] +
        "<br>time: " + input[3] + "</p>");

    /*for (i = 0; i < 4; i++) {
        alert(input[i]);
    }*/


    var elem = {
        longitude: input[0],
        latitude: input[1],
        time: input[2]
    };

    $.getJSON("http://temp1.mar98.tk/HackNTU2015/forecast.php", elem, function(data) {
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

    event.preventDefault();

});