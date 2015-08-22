var input = [];
$("#submit").click(function() {
    input[0] = $('#longitude').val();
    input[1] = $('#latitude').val();
    input[2] = $('select[name="year"]').find(":selected").text();
    input[3] = $('select[name="month"]').find(":selected").text();
    input[4] = $('select[name="date"]').find(":selected").text();
    input[5] = $('select[name="hour"]').find(":selected").text();
    input[6] = $('select[name="minute"]').find(":selected").text();

    var $time = input[2]+"-"+input[3]+"-"+input[4]+" "+input[5]+":"+input[6]+":00";

    //show all elem for input
    /* 
    $("#show").append("<p>longitude: " + input[0] +
        "<br>latitude: " + input[1] +
        "<br>date: " + input[2] +
        "<br>time: " + input[3] + "</p>");
    */

    /*for (i = 0; i < 4; i++) {
        alert(input[i]);
    }*/


    var elem = {
        longitude: input[0],
        latitude: input[1],
        time: $time
    };

    $.getJSON("http://temp2.mar98.tk/HackNTU2015/forecast.php", elem, function(data) {

        if (data["status"] == "success") {
            //alert("success");
            var items = [];
            $.each(data["result"], function(key, val) {
                items.push("<p> The " + key + " is " + val + ".</p>");
            });

            $("#show").append(items.join(""));
        } else {
            alert("error");
        }

        /*$("<ul/>", {
            "class": "my-new-list",
            html: items.join("")
        }).appendTo("#show");*/
    });

    event.preventDefault();

});