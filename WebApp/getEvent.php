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
        echo '<input type="text" id="text-input" name="text-input" value="' . pg_fetch_result($HdrQuery, 0, 1) . '" class="form-control" readonly>';
        echo '</div>';
        echo '</div>';

        echo '<div class="row form-group">';
        echo '<div class="col col-md-3">';
        echo '<label for="textarea-input" class=" form-control-label">Event Description</label>';
        echo '</div>';
        echo '<div class="col-12 col-md-9">';
        echo '<textarea name="textarea-input" id="textarea-input" rows="9" class="form-control" readonly>' . pg_fetch_result($HdrQuery, 0, 3) . '</textarea>';
        echo '</div>';
        echo '</div>';

        echo '<div class="row form-group">';
        echo '<div class="col-12">';
        echo '<label for="select" class=" form-control-label">Game List</label>';
        echo '</div>';

        pg_free_result($HdrQuery);

        $DtlQuery = pg_prepare($dbconn, 'FetchEventDtlStatement', 'SELECT * FROM Event_Detail left join Games on Event_Detail.eGameId = Games.id where eDtlHdrId = $1');
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
                echo '<td>' . $result[5] . '</td><td>' . $result[4] . '</td>';
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
