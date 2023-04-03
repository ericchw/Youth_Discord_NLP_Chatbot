<?php

// $webhookurl should be like $webhookurl = "https://discord.com/api/webhooks/1083624411099304027/3vnRCa53jBNiMV4pnsgJ8yNwu_Svxaoxc6j_9PN85d0a_uHfFSog-XK7kN0jlvQvzXE7"
//=======================================================================================================
// Compose message. You can use Markdown
// Message Formatting -- https://discordapp.com/developers/docs/reference#message-formatting
//========================================================================================================

$id = $_POST['eventId'];

// include 'dbconfig.php';
// include __DIR__ . '/vendor/autoload.php';

// $dbconn = pg_connect("host=$dbhost dbname=$dbname user=$dbuser password=$dbpass")
//     or die('Could not connect: ' . pg_last_error());

// $query = pg_prepare($dbconn, 'SelectAndPostStatement', 'select * FROM EVENT WHERE EVTId = $1');
// $query = pg_execute($dbconn, 'SelectAndPostStatement', array($id));

    $url = 'http://python/create_event/' . $id;
    PostData($url);
    header('Location: event_page.php');
    // pg_free_result($query);
    // pg_close($dbconn);
    //header('Location: event_page.php?erro=There is error on posting to Discord Bot');
    // pg_free_result($query);
    // pg_close($dbconn);

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
