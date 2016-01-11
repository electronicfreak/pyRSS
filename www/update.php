<?
	error_reporting(E_ALL);
	ini_set('display_errors', '1');

	require('func.php');
	if(isset($_POST['url']) && isset($_POST['data']) && isset($_POST['cat'])) {
		//print_r($_POST);

		$url = chkGet($_POST['url']);
		$data = chkGet($_POST['data']);
		$cat = chkGet($_POST['cat']);
		mysql_query("INSERT INTO urls (url, data, cat) VALUES ('{$url}','{$data}','{$cat}')");
		//echo mysql_error();	
		if(mysql_affected_rows() > 0) {
			echo 'OK';
		}else{
			echo 'ERROR';
		}
	}
?>