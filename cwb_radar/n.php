<?php
require_once('conf.php');
require_once('CWB_Radar.php');
require_once('radar.php');

$mysqli = new mysqli("localhost", mysql_user, mysql_pass, 'cwb_data');

if (mysqli_connect_errno()) {
	printf("Connect failed: %s\n", mysqli_connect_error());
	exit();
}
$mysqli->set_charset("utf8");

$data = get_radar_at_N();

foreach($data as $m) {
	$c = CWB_Radar::get($mysqli, 'n', $m['time']);
	if (is_null($c)) {
		$filename = basename($m['url']);
		echo $filename . ' should download' . "\n";
		
		get_radar_image($m['url'], 'img/' . $filename);

		CWB_Radar::insert($mysqli, 'n', $m['time'], $filename);
	}
}

$mysqli->close();
