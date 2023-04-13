<?php

$id = $_POST['pollid'];

include 'dbconfig.php';

$dbconn = pg_connect("host=$dbhost dbname=$dbname user=$dbuser password=$dbpass")
    or die('Could not connect: ' . pg_last_error());

$query = pg_prepare($dbconn, 'RejectPollingStatement', 'UPDATE Polling SET POLLStatus=$1 WHERE pollid = $2');
$query = pg_execute($dbconn, 'RejectPollingStatement', array('Rejected', $id));

if ($query) {
    header('Location: eventDtl_page.php?succ=This apply has been rejected');
    pg_free_result($query);
    pg_close($dbconn);
} else {
    header('Location: eventDtl_page.php?erro=There is some error when trying to delete a username');
    pg_free_result($query);
    pg_close($dbconn);
}
