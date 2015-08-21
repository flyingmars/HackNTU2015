<?php

class CWB_Radar {
	static public function get($conn, $type, $date) {
		$stmt = $conn->prepare("SELECT `filename` FROM `radar` WHERE `type`=? AND `date`=?");
		$stmt->bind_param('ss', $type, $date);
		$stmt->execute();

		$stmt->bind_result($filename);

		if ($stmt->fetch()) {
			return array(
				'type' => $type,
				'date' => $date,
				'filename' => $filename
			);
		}
		return NULL;
	}
	static public function insert($conn, $type, $date, $filename) {
		$stmt = $conn->prepare("INSERT INTO `radar` SET `type`=?, `date`=?, `filename`=?");
		$stmt->bind_param('sss', $type, $date, $filename);
		$stmt->execute();
	}
}
