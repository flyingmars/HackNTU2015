<?php
exec('git pull', $outputs);
header("Content-Type:text/plain");
foreach($outputs as $output) {
	echo $output . "\n";
}
