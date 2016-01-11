<?
	require('func.php');

	if(isset($_POST['url']) && isset($_POST['data'])) {
		$url = chkGet($_POST['url']);
		$data = chkGet($_POST['data'])
		mysql_query("INSERT INTO url (url, data) VALUES ('{$url}','{$data}')");
		if(mysql_affected_rows() > 0) {
			echo 'OK';
		}else{
			echo 'ERROR';
		}
	}
?>
