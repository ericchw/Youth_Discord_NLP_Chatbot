<?php
include 'dbconfig.php';

$dbconn = pg_connect("host=$dbhost dbname=$dbname user=$dbuser password=$dbpass")
    or die('Could not connect: ' . pg_last_error());


$query = pg_query($dbconn, 'SELECT * FROM Activity');

if (pg_num_rows($query) > 0) {
    echo '<select name="aty" id="aty" style="width:100%;" required>';
    echo '<option></option>';
    while ($result = pg_fetch_array($query)) {
        echo '<option value="' . $result['atyid'] . '">' . $result['atyname'] . '</option>';
    }

    echo '</select>';
    pg_free_result($query);
    pg_close($dbconn);
} else {
    pg_free_result($query);
    pg_close($dbconn);
}
