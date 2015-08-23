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

    var elem = {
        longitude: input[0],
        latitude: input[1],
        time: $time
    };

    $.getJSON("http://temp2.mar98.tk/HackNTU2015/forecast.php", elem, function(data) {
        $("#jump-body").empty();
    	// logging the results
    	console.log(data);

        if (data["status"] == "success") {
            var items = [];

            var output = "降雨機率是 " + data["result"]["risklevel"] / 255; 

            $("#jump-body").append(output);
        } else {
            $("#jump-body").append("error");
        }
    });
    event.preventDefault();
});

function initMap() {
  var geocoder = new google.maps.Geocoder();
  $("#location_submit").click(function(e){
	geocodeAddress(geocoder);
	e.preventDefault();
  });
}

function geocodeAddress(geocoder) {
  var location = document.getElementById('location').value;
  geocoder.geocode({'address': location}, function(results, status) {
    if (status === google.maps.GeocoderStatus.OK) {
	  $("#latitude").val(results[0].geometry.location.G);
	  $("#longitude").val(results[0].geometry.location.K);
    } else {
      console.log('Geocode was not successful for the following reason: ' + status);
    }
  });
}
