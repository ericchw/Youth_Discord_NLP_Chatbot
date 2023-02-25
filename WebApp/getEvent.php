<?php
function getEventById($id)
{

    include 'dbconfig.php';

    $dbconn = pg_connect("host=$dbhost dbname=$dbname user=$dbuser password=$dbpass")
        or die('Could not connect: ' . pg_last_error());

    $HdrQuery = pg_prepare($dbconn, 'FetchEventHdrStatement', 'SELECT * FROM Event_Header where eHdrId = $1');
    $HdrQuery = pg_execute($dbconn, 'FetchEventHdrStatement', array($id));

    if (pg_num_rows($HdrQuery) != 0) {

        echo '<div class="row form-group">';
        echo '<div class="col col-md-3">';
        echo '<label for="text-input" class=" form-control-label">Title</label>';
        echo '</div>';
        echo '<div class="col-12 col-md-9">';
        echo '<input type="text" id="text-input" name="text-input" value="' . pg_fetch_result($HdrQuery, 0, 'ehdrtitle') . '" class="form-control" readonly>';
        echo '</div>';
        echo '</div>';

        echo '<div class="row form-group">';
        echo '<div class="col col-md-3">';
        echo '<label for="textarea-input" class=" form-control-label">Event Description</label>';
        echo '</div>';
        echo '<div class="col-12 col-md-9">';
        echo '<textarea name="textarea-input" id="textarea-input" rows="9" class="form-control" readonly>' . pg_fetch_result($HdrQuery, 0, 'ehdrdesc') . '</textarea>';
        echo '</div>';
        echo '</div>';

        echo '<div class="row form-group">';
        echo '<div class="col-12">';
        echo '<label for="select" class=" form-control-label">Game List</label>';
        echo '</div>';

        pg_free_result($HdrQuery);

        $DtlQuery = pg_prepare($dbconn, 'FetchEventDtlStatement', 'SELECT * FROM Event_Detail left join Games on Event_Detail.eDtlGameId = Games.id where eDtlHdrId = $1');
        $DtlQuery = pg_execute($dbconn, 'FetchEventDtlStatement', array($id));

        if (pg_num_rows($DtlQuery) != 0) {
            echo '<div class="col-lg-12">';
            echo '<div class="table-responsive table--no-card m-b-30">';
            echo '<table class="table table-borderless table-striped table-earning">';
            echo '<thead>';
            echo '<tr>';
            echo '<th>Chinese Name</th>';
            echo '<th>English Name</th>';
            echo '</tr>';
            echo '</thead>';
            echo '<tbody>';
            while ($result = pg_fetch_array($DtlQuery)) {
                echo '<tr>';
                echo '<td>' . $result['name_zh'] . '</td><td>' . $result['name'] . '</td>';
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

function searchEventById($key)
{

    include 'dbconfig.php';

    $dbconn = pg_connect("host=$dbhost dbname=$dbname user=$dbuser password=$dbpass")
        or die('Could not connect: ' . pg_last_error());
        // position($1 in eHdrTitle) > 0
    $key = strtoupper($key);
    $query = pg_prepare($dbconn, 'SearchEventHdrStatement', 'SELECT * FROM Event_Header WHERE position($1 in UPPER(eHdrTitle)) > 0 ORDER BY eHdrCreateDate desc');
    $query = pg_execute($dbconn, 'SearchEventHdrStatement', array($key));

    if (pg_num_rows($query) > 0) {
        echo '<tbody>';
        while ($result = pg_fetch_array($query)) {
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
}
