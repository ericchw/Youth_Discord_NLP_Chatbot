<?php
include 'dbconfig.php';

$dbconn = pg_connect("host=$dbhost dbname=$dbname user=$dbuser password=$dbpass")
    or die('Could not connect: ' . pg_last_error());

$query = pg_query($dbconn, 'SELECT * FROM Games');

if (pg_num_rows($query) > 0) {
    echo '<tbody>';
    while ($result = pg_fetch_array($query)) {
        echo '<tr class="tr-shadow">';
        echo '<td>
        <div>
            <form action="deleteGame.php" method="POST">
                <button class="btn btn-danger" data-toggle="tooltip" data-placement="top" title="Delete" name="gameId" value="' . $result[0] . '">
                    X
                </button>
            </form>
        </div>
        </td>';
        echo '<td>' . $result[2] . '</td>';
        echo '<td>' . $result[1] . '</td>';
        echo '<tr class="spacer"></tr>';
    }

    echo '</tbody>';
    pg_free_result($query);
    pg_close($dbconn);
} else {
    echo 'No data';
    pg_free_result($query);
    pg_close($dbconn);
}
