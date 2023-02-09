<?php

session_start();
$_SESSION = array(); 
unset($_COOKIE['email']);
unset($_COOKIE['username']);
session_destroy();
header('Location: login_page.php');
