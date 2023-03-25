<?php
function insertGame($atyName)
{

    include 'dbconfig.php';

    $dbconn = pg_connect("host=$dbhost dbname=$dbname user=$dbuser password=$dbpass")
        or die('Could not connect: ' . pg_last_error());

    date_default_timezone_set('Asia/Hong_Kong');
    $now = date('Y-m-d H:i:s', time());

    $query = pg_prepare($dbconn, 'InsertGameStatement', 'INSERT INTO Activity(atyid, atyname, atycreatedate, atyupdatedate) VALUES (DEFAULT, $1, $2, $3)');
    $query = pg_execute($dbconn, 'InsertGameStatement', array($atyName, $now, $now));

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
        header('Location: activityList_page.php?succ=Create Successfully');

        pg_free_result($query);
        pg_close($dbconn);
    }
}
if (isset($_POST['submit'])) {
    $atyName = $_POST['name'];
    insertGame($atyName);
}
