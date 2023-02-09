<?php

    include 'dbconfig.php';

    $dbconn = pg_connect("host=$dbhost dbname=$dbname user=$dbuser password=$dbpass")
        or die('Could not connect: ' . pg_last_error());

    $query = pg_query($dbconn, 'SELECT * FROM Games');
    //$query = pg_execute($dbconn, 'FetchEventStatement');

    if (pg_num_rows($query) > 0) {
        while($result = pg_fetch_array($query)) {
            echo '<option value="' . $result[0] . '">' . $result[1] . ' - ' . $result[2];
        }

        pg_free_result($query);
        pg_close($dbconn);
    } else {
        pg_free_result($query);
        pg_close($dbconn);
    }

