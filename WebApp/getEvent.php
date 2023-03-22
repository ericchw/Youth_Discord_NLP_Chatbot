<?php
function getEventById($id)
{

    include 'dbconfig.php';

    $dbconn = pg_connect("host=$dbhost dbname=$dbname user=$dbuser password=$dbpass")
        or die('Could not connect: ' . pg_last_error());

    $HdrQuery = pg_prepare($dbconn, 'FetchEventHdrStatement', 'SELECT * FROM Event left join Activity on Event.atyid = Activity.atyid where evtid = $1');
    $HdrQuery = pg_execute($dbconn, 'FetchEventHdrStatement', array($id));

    if (pg_num_rows($HdrQuery) != 0) {
        echo '<div class="row form-group">';
        echo '<div class="col col-md-3">';
        echo '<label for="text-input" class=" form-control-label">Title</label>';
        echo '</div>';
        echo '<div class="col-12 col-md-9">';
        echo '<input type="text" id="text-input" name="text-input" value="' . pg_fetch_result($HdrQuery, 0, 'evttitle') . '" class="form-control" readonly>';
        echo '</div>';
        echo '</div>';

        echo '<div class="row form-group">';
        echo '<div class="col col-md-3">';
        echo '<label for="title" class=" form-control-label">Activity</label>';
        echo '</div>';
        echo '<div class="col-12 col-md-9">';
        echo '<input type="text" id="text-input" name="text-input" value="' . pg_fetch_result($HdrQuery, 0, 'atyname') . '" class="form-control" readonly>';
        echo '</div>';
        echo '</div>';

        echo '<div class="row form-group">';
        echo '<div class="col col-md-3">';
        echo '<label for="textarea-input" class=" form-control-label">Event Description</label>';
        echo '</div>';
        echo '<div class="col-12 col-md-9">';
        echo '<textarea name="textarea-input" id="textarea-input" rows="9" class="form-control" readonly>' . pg_fetch_result($HdrQuery, 0, 'evtdesc') . '</textarea>';
        echo '</div>';
        echo '</div>';

        echo '<div class="row form-group">';
        echo '<div class="col col-md-3">';
        echo '<label for="maxMember" class=" form-control-label">Maximum Number of Member</label>';
        echo '</div>';
        echo '<div class="col-12 col-md-9">';
        echo '<input type="number" id="maxMember" name="maxMember" value="' . pg_fetch_result($HdrQuery, 0, 'evtlimitmem') . '" class="form-control" readonly>';
        echo '</div>';
        echo '</div>';

        echo '<div class="row form-group">';
        echo '<div class="col col-md-3">';
        echo '<label for="eventDate" class=" form-control-label">Date</label>';
        echo '</div>';
        echo '<div class="col-12 col-md-9">';
        echo '<input type="datetime-local" id="eventDate" name="eventDate" value="' . pg_fetch_result($HdrQuery, 0, 'evtdate') . '"class="form-control" readonly>';
        echo '</div>';
        echo '</div>';
        echo '<br />';

        pg_free_result($HdrQuery);

        $DtlQuery = pg_prepare($dbconn, 'FetchPollingStatement', 'SELECT * FROM polling WHERE evtid = $1');
        $DtlQuery = pg_execute($dbconn, 'FetchPollingStatement', array($id));

        if (pg_num_rows($DtlQuery) != 0) {
            echo '<div class="col-lg-12">';
            echo '<div class="table-responsive table--no-card m-b-30">';
            echo '<table class="table table-borderless table-striped table-earning">';
            echo '<thead>';
            echo '<tr>';
            echo '<th></th>';
            echo '<th>Discord ID</th>';
            echo '<th>Discord Name</th>';
            echo '</tr>';
            echo '</thead>';
            echo '<tbody>';
            while ($result = pg_fetch_array($DtlQuery)) {
                echo '<tr>';
                echo '<td><button class="btn btn-danger" data-toggle="tooltip" data-placement="top" title="Delete" name="polldcid" value="' . $result['polldcid'] . '">X</button></td>';
                echo '<td>' . $result['polldcid'] . '</td><td>' . $result['polldcusername'] . '</td>';
                echo '</tr>';
            }

            echo '</table>';
            echo '</tbody>';
            echo '</div>';
        }
        echo '</div>';
        echo '</div>';

        pg_free_result($DtlQuery);
        pg_close($dbconn);
    }
    //header('Location: login_page.php?erro=Username or password incorrect');

}

function searchEventByKey($key)
{

    include 'dbconfig.php';

    $dbconn = pg_connect("host=$dbhost dbname=$dbname user=$dbuser password=$dbpass")
        or die('Could not connect: ' . pg_last_error());
    // position($1 in eHdrTitle) > 0
    $key = strtoupper($key);
    $query = pg_prepare($dbconn, 'SearchEventHdrStatement', 'SELECT * FROM Event WHERE position($1 in UPPER(evttitle)) > 0 ORDER BY evtcreatedate desc');
    $query = pg_execute($dbconn, 'SearchEventHdrStatement', array($key));

    if (pg_num_rows($query) > 0) {
        echo '<tbody>';
        while ($result = pg_fetch_array($query)) {
            echo '<tr class="tr-shadow">';
            echo '<td>' . $result['evttitle'] . '</td>';
            echo '<td class="desc">' . $result['evtdesc'] . '</td>';
            echo '<td>' . $result['evtdate'] . '</td>';
            echo '<td>' . $result['evtlimitmem'] . '</td>';
            echo '<td>
                        <div class="table-data-feature">
                            <form  action="postEvent.php" method="POST">
                                <button class="item" data-toggle="tooltip" data-placement="top" title="" data-original-title="Post on Discord" name="eventId" value="' . $result['evtid'] . '">
                                    <i class="zmdi zmdi-mail-send"></i>
                                </button>
                            </form>
                            <form action="eventDtl_page.php" method="POST">
                                <button class="item" data-toggle="tooltip" data-placement="top" title="View Details" name="eventId" value="' . $result['evtid'] . '">
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
}
