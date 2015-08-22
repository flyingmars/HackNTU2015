<?php
$latitude = $_GET['latitude'];
$longitude = $_GET['longitude'];
$time = $_GET['time'];

if (is_null($latitude) || is_null($longitude) || is_null($time)) {
	header("Access-Control-Allow-Origin: *");
	header("Access-Control-Allow-Methods: *");
	header("Content-Type: application/json");
	echo json_encode(array('status' => 'error'));
	exit;
}

// probability in [0,1]
// Intensity in mm/day
$output = array(
	'latitude' => $latitude, 
	'longitude' => $longitude,
	'time' => $time,
	'probability' => 0.9,
	'intensity' => 3.0
);

header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: *");
header("Content-Type: application/json");
echo json_encode(array('status' => 'success', 'result' => $output));
