<?
	require('func.php');
	// startseite
	$res = mysql_query("SELECT * FROM urls ORDER BY cat,ts");
	$num = mysql_num_rows($res);
	echo '<h1>RSS</h1>';
	$cat = '';
	for($i=0;$i<$num;$i++) {
		$a = mysql_fetch_assoc($res);
		if($cat != $a['cat']) {
			echo '<h2>'. $a['cat'] .'</h2>';
			$cat= $a['cat'];
		}
		echo '<a href="link.php?id='.$a['id'].'" style="display:block; margin-bottom:10px;">'. nl2br($a['data']) .'</a>';
	}
?>
