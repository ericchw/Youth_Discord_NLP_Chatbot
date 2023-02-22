<?php
function insertEvent($title, $desc, $limit, $date)
{

    include 'dbconfig.php';

    $dbconn = pg_connect("host=$dbhost dbname=$dbname user=$dbuser password=$dbpass")
        or die('Could not connect: ' . pg_last_error());

    $now = new DateTime();
    //$now->getTimestamp();   

    echo $now . '  ';

    //$query = pg_prepare($dbconn, 'InsertEventStatement', 'INSERT INTO Event_Header(eHdrId, eHdrTitle, eHdrStatus, eHdrDesc, eHdrLimitMem, eHdrDate, eHdrCreateDate) VALUES (DEFAULT, $1, $2, $3, $4, $5, $6)');
    //$query = pg_execute($dbconn, 'InsertEventStatement', array($title, 'Pending', $desc, $limit, $date, $now));

    // if (pg_num_rows($query) != 0) {
    //     pg_free_result($query);
    //     pg_close($dbconn);
    //     header('Location: index_page.php');
    // } else {
    //     pg_free_result($query);
    //     pg_close($dbconn);
    //     header('Location: login_page.php?erro=Username or password incorrect');
    // }
    if ($query) {
        //header('Location: event_page.php');

        pg_free_result($query);
        pg_close($dbconn);
    }
}
if (isset($_POST['submit'])) {
    $title = $_POST['title'];
    $desc = $_POST['desc'];
    $limit = $_POST['maxMember'];
    $date = $_POST['eventDate'];
    insertEvent($title, $desc, $limit, $date);
}
