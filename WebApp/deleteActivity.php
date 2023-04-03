<?php
$id = $_POST['atyid'];

include 'dbconfig.php';

$dbconn = pg_connect("host=$dbhost dbname=$dbname user=$dbuser password=$dbpass")
    or die('Could not connect: ' . pg_last_error());

$query = pg_prepare($dbconn, 'DeleteActivityStatement', 'DELETE FROM Activity WHERE atyid = $1');
$query = pg_execute($dbconn, 'DeleteActivityStatement', array($id));

if ($query) {
    header('Location: activityList_page.php');
    pg_free_result($query);
    pg_close($dbconn);
} else {
    header('Location: activityList_page.php?erro=There is some error when trying to delete a activity');
    pg_free_result($query);
    pg_close($dbconn);
}
