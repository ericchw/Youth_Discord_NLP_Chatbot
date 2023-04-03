<?php

include 'dbconfig.php';

$dbconn = pg_connect("host=$dbhost dbname=$dbname user=$dbuser password=$dbpass")
    or die('Could not connect: ' . pg_last_error());

$query = pg_query($dbconn, 'SELECT * FROM Event ORDER BY EVTCreateDate desc');
//$query = pg_execute($dbconn, 'FetchEventStatement');

if (pg_num_rows($query) > 0) {
    echo '<tbody>';
    while ($result = pg_fetch_array($query)) {
        echo '<tr class="tr-shadow">';
        echo '<td>' . $result['evttitle'] . '</td>';
        echo '<td class="desc">' . $result['evtdesc'] . '</td>';
        echo '<td>' . $result['evtdate'] . '</td>';
        echo '<td>' . $result['evtdeadline'] . '</td>';
        echo '<td>' . $result['evtlimitmem'] . '</td>';
        echo '<td>
                    <div class="table-data-feature">
                        <form  action="postEvent.php" method="POST">
                            <button class="item" data-toggle="tooltip" data-placement="top" title="" data-original-title="Post on Discord" name="eventId" value="' . $result['evtid'] . '" onclick="return confirm(\'Are you sure post this event to discord?\')" >
                                <i class="zmdi zmdi-mail-send"></i>
                            </button>
                        </form>
                        <form action="eventDtl_page.php" method="POST">
                            <button class="item" data-toggle="tooltip" data-placement="top" title="View Details" name="eventId" value="' . $result['evtid'] . '"">
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
