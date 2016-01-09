<?
	require('secret.php');
	// startseite
	$res = mysql_query("SELECT * FROM urls ORDER BY cat,ts");
	$num = mysql_num_rows($res);
	echo '<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">';
	$cat = '';
	for($i=0;$i<$num;$i++) {
		$a = mysql_fetch_assoc($res);
		if($cat != $a['cat']) {
			if($cat != '') {
				echo '</channel>';
			}
			echo '<channel><title>'. $a['cat'] .'</title><link>http://rss.electronicfreak.de</link><description></description>';
		}
		echo '<item><title>'. $a['ts'] .'</title><link>http://rss.electronicfreak.de/link.php?id='.$a['id'].'</link><description>'. nl2br($a['data']) .'</description></item>';
	}
?></channel></rss>