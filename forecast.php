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

$cmd = 'python ./queryTools/queryPixelFromPos.py ' . escapeshellarg($latitude) . ' ' . escapeshellarg($longitude);
$pixel = run($cmd);

header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: *");
header("Content-Type: application/json");
echo json_encode(array('status' => 'success', 'result' => array(
	'latitude' => $latitude, 
	'longitude' => $longitude,
	'time' => $time,
	'pixel' => $pixel,
	'probability' => 0.9,
	'intensity' => 3.0
)));

function run($cmd) {
	exec($cmd, $outputs);
	return json_decode($outputs[0], true);
}
