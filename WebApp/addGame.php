<?php
function insertGame($engName, $ehName)
{

    include 'dbconfig.php';

    $dbconn = pg_connect("host=$dbhost dbname=$dbname user=$dbuser password=$dbpass")
        or die('Could not connect: ' . pg_last_error());

    $query = pg_prepare($dbconn, 'InsertGameStatement', 'INSERT INTO Games(id, name, name_zh) VALUES (DEFAULT, $1, $2)');
    $query = pg_execute($dbconn, 'InsertGameStatement', array($engName, $ehName));

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
        header('Location: gameList_page.php');

        pg_free_result($query);
        pg_close($dbconn);
    }
}
if (isset($_POST['submit'])) {
    $engName = $_POST['engName'];
    $ehName = $_POST['zhName'];
    insertGame($engName, $ehName);
}
