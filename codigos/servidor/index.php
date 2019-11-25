<?php 
$json = file_get_contents('php://input');
$data = json_decode($json);

$myfile = fopen("imagens.txt","w");
fwrite($myfile,$json);
fclose($myfile);
?>

