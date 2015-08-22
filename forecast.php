<?php

// probability in [0,1]
// Intensity in mm/day
$output = array('probability' => 0.9 , 'intensity' => 3.0 );

header("Access-Control-Allow-Origin: *");
header("Access-Control-Allow-Methods: *");
header("Content-Type: application/json");
echo json_encode($output) ;
