<?php

    include 'dbconfig.php';

    $dbconn = pg_connect("host=$dbhost dbname=$dbname user=$dbuser password=$dbpass")
        or die('Could not connect: ' . pg_last_error());

    $query = pg_query($dbconn, 'SELECT * FROM Event_Header');
    //$query = pg_execute($dbconn, 'FetchEventStatement');

    if (pg_num_rows($query) > 0) {
        echo '<tbody>';
        while($result = pg_fetch_array($query)) {
            echo '<tr class="tr-shadow">';
            echo '<td>' . $result[1] . '</td>';
            echo '<td class="desc">' . $result[3] . '</td>';
            echo '<td>' . $result[4] . '</td>';
            echo '<td><span class="status--process">' . $result[2] . '</span></td>';
            echo '<td>
                    <div class="table-data-feature">
                        <form action="viewEvent_page.php" method="POST">
                            <button class="item" data-toggle="tooltip" data-placement="top" title="View" name="eventId" value="' . $result[0] . '">
                                <i class="zmdi zmdi-assignment"></i>
                            </button>
                        </form>
                    </div>
                </td><tr class="spacer"></tr>';
        }

        echo '</tbody>';
        pg_free_result($query);
        pg_close($dbconn);
    } else {
        pg_free_result($query);
        pg_close($dbconn);
    }

