<?php

if (empty($_COOKIE['email'])) {
    header('Location: login_page.php?erro=Login expired');
}

