<?
	error_reporting(E_ALL);
	ini_set('display_errors', '1');
	
	require('secret.php');

        function chkGet($str,$allow=false) {
                $return = str_replace("'", "`", $str);
                $return = str_replace('"', "`", $return);
                if(!$allow)
                        $return = str_replace(strtolower('<script'),'&lt;script',$return);
                return $return;
        }

	// löschen wenn schonmal gesehen
	function seenData() {}

	// Favorit eintragen
	function addFav() {}

	// Favorit entfernen
	function remFav() {}


?>
