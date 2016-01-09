<?
	require('secret.php');
	
	function chkGet($str,$allow=false) {
		$return = str_replace("'", "`", $str);
		$return = str_replace('"', "`", $return);
		if(!$allow)
			$return = str_replace(strtolower('<script'),'&lt;script',$return);
		return $return;
	}
	
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