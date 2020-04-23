<?php

session_start();

$temp = exec("robot_test.py");
$temp = explode(" ", $temp);
$number = $temp[0];
$file = $temp[1];

$_SESSION['arquivo'] = $temp[1];

#$form = exec("aleatorio.py");

echo "
<!DOCTYPE html>
<html>
<head>
	<title>Você é um robô?</title>

	<style>
		div.corpo {
		  text-align: center;
		}
	</style>


</head>

<body>

<div class='corpo'>
<h2>Você é um robô?</h2>
<p>Escolha a opção correspondente aos números da imagem abaixo para poder passar:</p>
<br>

<img src='$file' alt='Numeros'>
<form method='POST' action='resultado_robot_test.php'>
			<input size='12' type='text' placeholder='123456' id = 'numeros' name='numeros'/><br>
			<br>
			<input type='submit' style='background-color: #4CAF50; font-family:arial; font-size:15px; color: white; text-align: center; width:150px; height:40px' value='Testar'/>
</form>

</div>
</body>";


#echo $form;

#echo "

?>