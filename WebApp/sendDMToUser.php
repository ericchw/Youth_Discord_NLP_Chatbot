<?php

session_start();

$id = $_SESSION["eventid"];

$url = 'http://python_api/send_message/' . $id;
PostData($url);
header('Location: eventDtl_page.php?succ=Send the message successfully');

function PostData($url)
{
    $curl = curl_init($url);
    curl_setopt($curl, CURLOPT_URL, $url);
    curl_setopt($curl, CURLOPT_FOLLOWLOCATION, 1);
    curl_setopt($curl, CURLOPT_HEADER, 0);
    curl_setopt($curl, CURLOPT_RETURNTRANSFER, 1);
    curl_exec($curl);
    curl_close($curl);
}
