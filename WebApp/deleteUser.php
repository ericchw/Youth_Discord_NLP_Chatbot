<?php

$id = $_POST['pollid'];

include 'dbconfig.php';

$dbconn = pg_connect("host=$dbhost dbname=$dbname user=$dbuser password=$dbpass")
    or die('Could not connect: ' . pg_last_error());

$query = pg_prepare($dbconn, 'DeletePollingStatement', 'DELETE FROM Polling WHERE pollid = $1');
$query = pg_execute($dbconn, 'DeletePollingStatement', array($id));

if ($query) {
    header('Location: event_page.php?succ=Delete Successfully');
    pg_free_result($query);
    pg_close($dbconn);
} else {
    header('Location: event_page.php?erro=There is some error when trying to delete a username');
    pg_free_result($query);
    pg_close($dbconn);
}
