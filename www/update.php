<?
	error_reporting(E_ALL);
	ini_set('display_errors', '1');

	require('func.php');
	if(isset($_POST['url']) && isset($_POST['data']) && isset($_POST['cat'])) {
		//print_r($_POST);

		$url = chkGet($_POST['url']);
		$data = chkGet($_POST['data']);
		$title = chkGet($_POST['title']);
		$cat = chkGet($_POST['cat']);
		$url = str_replace("&amp;","&",$url);
		mysql_query("INSERT INTO urls (url, data, title, cat) VALUES ('{$url}','{$data}','{$title}','{$cat}')");
		//echo mysql_error();	
		if(mysql_affected_rows() > 0) {
			echo 'OK';
		}else{
			echo 'ERROR';
		}
	}
	
	if(isset($_GET['title'])) {		
		$title = chkGet($_GET['title']);		
		mysql_query("INSERT INTO urls (title, cat) VALUES ('{$title}','GET-Input')");
		if(mysql_affected_rows() > 0) {
			echo 'OK';
		}else{
			echo 'ERROR';
		}
	}
?>