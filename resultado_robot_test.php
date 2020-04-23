<?php

session_start();

set_time_limit(900);
$numeros = $_POST["numeros"];
$teste = '0';
$arquivo = $_SESSION['arquivo'];

#############################teste
#########################

if ($numeros.".png" == $arquivo) { 
 
 
 	echo '<!DOCTYPE html>
 	<html>
 	<head>
 		<title>Resultados</title>
 		<style>
 			table, th, td {
 			  border: 1px solid black;
 			  border-collapse: collapse;
 			  font-family: century gothic
 			}
 			th, td {
 			  padding: 5px;
 			  text-align: center;
 			}
 			table#t01 tr:nth-child(even) {
 			  background-color: #eee;
 			}
 			table#t01 tr:nth-child(odd) {
 			 background-color: #fff;
 			}
 			table#t01 th {
 			  background-color: black;
 			  color: white;
 			}
 		</style>
 	</head>
 
 	<body>
 	<div align="center">
 		<h1 style="border-style: solid; color: #0000ff; font-family:courier; width:720px; height:40px;">Você não é um robô!</h1>
 		<p style="border-style: solid; color: #33cc33; font-family:courier; width:350px; height:20px;">Parabéns! Você não é um robô!</p>';
 

 	echo "
 	</div>
 	</body>
 	</html>";
	exec("del $numeros.png"); 
 	#print($space);
 
 	#print($fundos);
}
	
else {
	exec("del $arquivo");
	echo "
	<!DOCTYPE html>
 	<html>
 	<head>
 		<title>Robô</title>
	</head>

	<body>
	<p>Desculpe, mas eu acho que você é um robô.</p>
	</body>
";
	 #echo $numeros;	
}




?>
