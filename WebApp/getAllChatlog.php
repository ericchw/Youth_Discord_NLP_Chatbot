<?php

    include 'dbconfig.php';

    $dbconn = pg_connect("host=$dbhost dbname=$dbname user=$dbuser password=$dbpass")
        or die('Could not connect: ' . pg_last_error());

    $query = pg_query($dbconn, 'SELECT * FROM Chatlog');
    //$query = pg_execute($dbconn, 'FetchEventStatement');

    if (pg_num_rows($query) > 0) {
        echo '<tbody>';
        while($result = pg_fetch_array($query)) {
            echo '<tr class="tr-shadow">';
            echo '<td>' . $result[1] . '</td>';
            echo '<td class="desc">' . $result[2] . '</td>';
            echo '<td>' . $result[3] . '</td>';
            echo '<td><span class="status--process">' . $result[4] . '</span></td>';
            echo '<td>' . $result[5] . '</td>';
            echo '<tr class="spacer"></tr>';
        }

        echo '</tbody>';
        pg_free_result($query);
        pg_close($dbconn);
    } else {
        pg_free_result($query);
        pg_close($dbconn);
    }

