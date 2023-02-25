<?php

include 'dbconfig.php';

$dbconn = pg_connect("host=$dbhost dbname=$dbname user=$dbuser password=$dbpass")
    or die('Could not connect: ' . pg_last_error());

$query = pg_query($dbconn, 'SELECT * FROM Event_Header ORDER BY eHdrCreateDate desc');
//$query = pg_execute($dbconn, 'FetchEventStatement');

if (pg_num_rows($query) > 0) {
    echo '<tbody>';
    while ($result = pg_fetch_array($query)) {
        //print_r($result['ehdrtitle']);
        echo '<tr class="tr-shadow">';
        echo '<td>' . $result['ehdrtitle'] . '</td>';
        echo '<td class="desc">' . $result['ehdrdesc'] . '</td>';
        echo '<td>' . $result['ehdrdate'] . '</td>';
        echo '<td><span class="status--process">' . $result['ehdrstatus'] . '</span></td>';
        echo '<td>' . $result['ehdrlimitmem'] . '</td>';
        echo '<td>
                    <div class="table-data-feature">
                        <form action="eventDtl_page.php" method="POST">
                            <button class="item" data-toggle="tooltip" data-placement="top" title="View" name="eventId" value="' . $result['ehdrid'] . '">
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
