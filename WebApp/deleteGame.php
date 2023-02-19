<?php
$id = $_POST['gameId'];

include 'dbconfig.php';

$dbconn = pg_connect("host=$dbhost dbname=$dbname user=$dbuser password=$dbpass")
    or die('Could not connect: ' . pg_last_error());

$query = pg_prepare($dbconn, 'DeleteEventStatement', 'DELETE FROM GAMES WHERE id = $1');
$query = pg_execute($dbconn, 'DeleteEventStatement', array($id));

if ($query) {
    header('Location: gameList_page.php');
    pg_free_result($query);
    pg_close($dbconn);
}
