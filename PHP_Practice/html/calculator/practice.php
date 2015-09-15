<?php
  $xml = simplexml_load_file('../xml/answer.xml');
  $ans = $xml->ansval;
  eval('$ans=' . $_POST['expression'] . ';');
  $xml->ansval = $ans;
  if (!$fp = fopen('../xml/answer.xml', 'w')) {
    echo "false";
  }
  fwrite($fp, $xml->asXML());
  fclose($fp);
  echo $ans;
?>