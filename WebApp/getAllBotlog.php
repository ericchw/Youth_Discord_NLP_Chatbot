<?php

include 'dbconfig.php';

$dbconn = pg_connect("host=$dbhost dbname=$dbname user=$dbuser password=$dbpass")
    or die('Could not connect: ' . pg_last_error());

$query = pg_query($dbconn, 'SELECT * FROM Botlog ORDER BY timestamp desc');
//$query = pg_execute($dbconn, 'FetchEventStatement');

if (pg_num_rows($query) > 0) {
    echo '<tbody>';
    while ($result = pg_fetch_array($query)) {
        echo '<tr class="tr-shadow">';
        echo '<td>' . $result['id'] . '</td>';
        echo '<td>' . $result['message'] . '</td>';
        echo '<td>' . $result['timestamp'] . '</td>';
        echo '<tr class="spacer"></tr>';
    }

    echo '</tbody>';
    pg_free_result($query);
    pg_close($dbconn);
} else {
    pg_free_result($query);
    pg_close($dbconn);
}
