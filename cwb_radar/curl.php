<?php
function query($url) {
	$curl = curl_init($url);

	curl_setopt($curl, CURLOPT_USERAGENT, "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.1) Gecko/20061204 Firefox/2.0.0.1");
	curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($curl, CURLOPT_HEADER, 1);

	$response = curl_exec($curl);
	$header_size = curl_getinfo($curl, CURLINFO_HEADER_SIZE);
	$header_string = substr($response, 0, $header_size);
	$body = substr($response, $header_size);

	$http_code = curl_getinfo($curl, CURLINFO_HTTP_CODE);

	return array('http_code'=> $http_code, 'body'=> $body);
}
