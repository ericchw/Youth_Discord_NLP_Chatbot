<?php
function login($email, $password)
{

    include 'dbconfig.php';

    $dbconn = pg_connect("host=$dbhost dbname=$dbname user=$dbuser password=$dbpass")
        or die('Could not connect: ' . pg_last_error());

    $query = pg_prepare($dbconn, 'LoginStatement', 'SELECT username FROM account where email= $1 and pwd= $2');
    $query = pg_execute($dbconn, 'LoginStatement', array($email, $password));

    if (pg_num_rows($query) != 0) {
        $username = pg_fetch_result($query, 0, 'username');
        if (isset($_COOKIE['email'])) {
            unset($_COOKIE['email']);
        }
        if (isset($_COOKIE['username'])) {
            unset($_COOKIE['username']);
        }
        setcookie('email', $email, time() + (60 * 30), "/");
        setcookie('username', $username, time() + (60 * 30), "/");
        pg_free_result($query);
        pg_close($dbconn);
        header('Location: index_page.php');
    } else {
        pg_free_result($query);
        pg_close($dbconn);
        header('Location: login_page.php?erro=Username or password incorrect');
    }
}
if (isset($_POST['submit'])) {
    $email = $_POST['email'];
    $pwd = md5($_POST['password']);
    login($email, $pwd);
}
?>