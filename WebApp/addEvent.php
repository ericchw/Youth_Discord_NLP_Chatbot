<?php
function insertEvent($title, $desc, $aty, $limit, $date)
{

    include 'dbconfig.php';

    $dbconn = pg_connect("host=$dbhost dbname=$dbname user=$dbuser password=$dbpass")
        or die('Could not connect: ' . pg_last_error());

    date_default_timezone_set('Asia/Hong_Kong');
    $now = date('Y-m-d H:i:s', time());

    $query = pg_prepare($dbconn, 'InsertEventStatement', 'INSERT INTO Event(evtid, atyid, evttitle, evtlimitmem, evtdesc, evtdate, evtcreatedate, evtupdatedate) 
                                                          VALUES (DEFAULT, $1, $2, $3, $4, $5, $6, $7)');
    $query = pg_execute($dbconn, 'InsertEventStatement', array($aty, $title, $limit, $desc, $date, $now, $now));

    if (pg_num_rows($query) == 0) {
        pg_free_result($query);
        pg_close($dbconn);
        header('Location: event_page.php');
    } else {
        pg_free_result($query);
        pg_close($dbconn);
        header('Location: login_page.php?erro=Username or password incorrect');
    }
}
if (isset($_POST['submit'])) {
    $title = $_POST['title'];
    $desc = $_POST['desc'];
    $aty = $_POST['aty'];
    $limit = $_POST['maxMember'];
    $date = $_POST['eventDate'];
    insertEvent($title, $desc, $aty, $limit, $date);
}
