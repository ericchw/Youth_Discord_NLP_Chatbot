<?php

if ($_COOKIE['email'] == null) {
    header('Location: login_page.php?erro=Login expired');
}

