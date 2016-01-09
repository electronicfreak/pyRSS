<?
	require('secret.php');
	// link weiterleitung
	if(isset($_GET['id'])) {
		if(is_numeric($_GET['id'])) {
			$res = mysql_query("SELECT url FROM urls WHERE id = '{$_GET['id']}'");
			if(mysql_num_rows($res) == 1) {
				$url = mysql_result($res,0);
				mysql_query("DELETE FROM urls WHERE id = '{$_GET['id']}'");
				header('Location: '. $url);
				die;
			}else{
				echo 'ERROR2';
			}
		}else{
			echo 'ERROR1';
		}
	}else{
		echo 'Eintrag nicht gefunden [<a href="index.php">weiter</a>]';
	}
?>