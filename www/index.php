<?
	require('func.php');
	// startseite
	$res = mysql_query("SELECT * FROM urls WHERE `seen` IS NULL ORDER BY cat,ts");
	echo mysql_error();
	$num = mysql_num_rows($res);
	echo '<h1>RSS</h1>';
	$cat = '';
	for($i=0;$i<$num;$i++) {
		$a = mysql_fetch_assoc($res);
		if($cat != $a['cat']) {
			echo '<h2>'. $a['cat'] .'</h2>';
			$cat= $a['cat'];
		}
		
		if($a['title'] == '') $a['title'] = '(kein Titel)';
		
		echo '<div><a href="link.php?id='.$a['id'].'" style="display:block; margin-bottom:10px;">'. nl2br($a['title']) .'</a><div>'. nl2br($a['data']) .'</div></div>';
	}
?>
