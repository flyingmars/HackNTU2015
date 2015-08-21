<?php
require_once('curl.php');

function get_radar_at_all() {
	$r = query('http://www.cwb.gov.tw/V7/js/MOS2_1024.js');
	$a = substr($r['body'], 16);

	preg_match_all('/\"(.*)\":\"(.*)\"/', $a, $matches, PREG_SET_ORDER);
	$data = array();
	foreach($matches as $match) {
		$data[] = array(
			'url'=> $match[1],
			'time' => str_replace('/', '-', $match[2])
		);
	}
	return $data;
}

function get_radar_image($url, $filename) {
	$r = query('http://www.cwb.gov.tw' . $url);
	file_put_contents($filename, $r['body']);
}
