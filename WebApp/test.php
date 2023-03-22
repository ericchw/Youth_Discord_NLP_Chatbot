<?php
include 'dbconfig.php';

$dbconn = pg_connect("host=$dbhost dbname=$dbname user=$dbuser password=$dbpass")
    or die('Could not connect: ' . pg_last_error());

$query = pg_query($dbconn, 'SELECT * FROM Event ORDER BY EVTCreateDate desc');

while ($result = pg_fetch_array($query)) {
    echo $result['evttitle'] . PHP_EOL;
}
pg_free_result($query);
pg_close($dbconn);
