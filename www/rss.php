<?
	header ("Content-Type:text/xml");
	require('func.php');
	// startseite
	$res = mysql_query("SELECT * FROM urls WHERE seen IS NULL ORDER BY cat,ts");
	$num = mysql_num_rows($res);
	echo '<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">';
	echo '<channel>
	<title></title>
	<link>http://rss.electronicfreak.de</link>
	<description></description>
';
	$cat = '';
	for($i=0;$i<$num;$i++) {
		$a = mysql_fetch_assoc($res);
		if($cat != $a['cat']) {
			$cat = $a['cat'];
			echo '</channel>
<channel>
	<title>'. $a['cat'] .'</title>
	<description></description>
';
		}
		
		$url = str_replace(array('=','&'),array('&#61;','&amp;'),$a['url'] );
		echo '	<item>
		<title>'. $a['title'] .'</title>
		<link>http://rss.electronicfreak.de/link.php?id='.$a['id'].'</link>
		<description>'. nl2br($a['data']) .'</description>
	</item>
';
	}
?></channel></rss>
