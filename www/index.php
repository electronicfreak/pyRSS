<?
	require('func.php');
	// startseite
	$res = mysql_query("SELECT * FROM urls ORDER BY ts");
	$num = mysql_num_rows($res);
	echo '<h1>RSS</h1>';
	for($i=0;$i<$num;$i++) {
		$a = mysql_fetch_assoc($res);
		echo '<a href="link.php?id='.$a['id'].'" style="display:block;">'. $a['cat'] .':'. nl2br($a['data']) .'</a>';
	}
?>
