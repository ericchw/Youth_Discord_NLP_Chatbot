<?php
function changePwd($email, $currPwd, $newPwd)
{

    include 'dbconfig.php';

    $dbconn = pg_connect("host=$dbhost dbname=$dbname user=$dbuser password=$dbpass")
        or die('Could not connect: ' . pg_last_error());

    $CheckLoginQuery = pg_prepare($dbconn, 'CheckLoginStatement', 'SELECT username FROM account where email= $1 and pwd= $2');
    $CheckLoginQuery = pg_execute($dbconn, 'CheckLoginStatement', array($email, $currPwd));

    if (pg_num_rows($CheckLoginQuery) != 0) {
        $UpdateQuery = pg_prepare($dbconn, 'UpdatePwdStatement', 'UPDATE account set pwd = $1 where email = $2');
        $UpdateQuery = pg_execute($dbconn, 'UpdatePwdStatement', array($newPwd, $email));

        pg_free_result($CheckLoginQuery);
        pg_free_result($UpdateQuery);
        pg_close($dbconn);
        header('Location: login_page.php?erro=Password Changed Successfully, please login again');
    } else {
        pg_free_result($query);
        pg_close($dbconn);
        header('Location: login_page.php?erro=Username or password incorrect');
    }
}
if (isset($_POST['submit'])) {
    $currPwd = md5($_POST['currPwd']);
    $newPwd = md5($_POST['newPwd']);
    $cnewPwd = md5($_POST['cnewPwd']);
    if ($_COOKIE['email'] == null) {
        header('Location: login_page.php?erro=Login expired');
    }
    $email = $_COOKIE['email'];
    if ($newPwd != $cnewPwd) {
        header('Location: changePassword.php?erro=New Password and Confirm New Password Not Match');
    } else {
        changePwd($email, $currPwd, $newPwd);
    }
}
