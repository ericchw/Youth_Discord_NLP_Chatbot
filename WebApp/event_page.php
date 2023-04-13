<?php
include 'checkCookie.php';
?>

<!DOCTYPE html>
<html lang="en">

<head>
  <!-- Required meta tags-->
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
  <meta name="description" content="au theme template" />
  <meta name="author" content="Hau Nguyen" />
  <meta name="keywords" content="au theme template" />

  <!-- Title Page-->
  <title>Event</title>

  <!-- Fontfaces CSS-->
  <link href="css/font-face.css" rel="stylesheet" media="all" />
  <link href="vendor/font-awesome-4.7/css/font-awesome.min.css" rel="stylesheet" media="all" />
  <link href="vendor/font-awesome-5/css/fontawesome-all.min.css" rel="stylesheet" media="all" />
  <link href="vendor/mdi-font/css/material-design-iconic-font.min.css" rel="stylesheet" media="all" />

  <!-- Bootstrap CSS-->
  <link href="vendor/bootstrap-4.1/bootstrap.min.css" rel="stylesheet" media="all" />

  <!-- Vendor CSS-->
  <link href="vendor/animsition/animsition.min.css" rel="stylesheet" media="all" />
  <link href="vendor/bootstrap-progressbar/bootstrap-progressbar-3.3.4.min.css" rel="stylesheet" media="all" />
  <link href="vendor/wow/animate.css" rel="stylesheet" media="all" />
  <link href="vendor/css-hamburgers/hamburgers.min.css" rel="stylesheet" media="all" />
  <link href="vendor/slick/slick.css" rel="stylesheet" media="all" />
  <link href="vendor/select2/select2.min.css" rel="stylesheet" media="all" />
  <link href="vendor/perfect-scrollbar/perfect-scrollbar.css" rel="stylesheet" media="all" />

  <!-- FullCalendar -->
  <link href="vendor/fullcalendar-3.10.0/fullcalendar.css" rel="stylesheet" media="all" />

  <!-- Main CSS-->
  <link href="css/theme.css" rel="stylesheet" media="all" />

  <style type="text/css">
    /* force class color to override the bootstrap base rule
       NOTE: adding 'url: #' to calendar makes this unneeded
     */
    .fc-event,
    .fc-event:hover {
      color: #fff !important;
      text-decoration: none;
    }
  </style>
</head>

<!-- animsition overrides all click events on clickable things like a,
      since calendar doesn't add href's be default,
      it leads to odd behaviors like loading 'undefined'
      moving the class to menus lead to only the menu having the effect -->

<body class="animsition">
  <div class="page-wrapper">
    <!-- HEADER MOBILE-->
    <header class="header-mobile d-block d-lg-none">
      <div class="header-mobile__bar">
        <div class="container-fluid">
          <div class="header-mobile-inner">
            <a class="logo" href="index_page.php">
              <img src="images/icon/logo.png" alt="CoolAdmin" />
            </a>
            <button class="hamburger hamburger--slider" type="button">
              <span class="hamburger-box">
                <span class="hamburger-inner"></span>
              </span>
            </button>
          </div>
        </div>
      </div>
      <nav class="navbar-mobile">
        <div class="container-fluid">
          <ul class="navbar-mobile__list list-unstyled">
            <li>
              <a href="index_page.php">
                <i class="fas fa-tachometer-alt"></i>Dashboard</a>
            </li>
            <li>
              <a href="activityList_page.php">
                <i class="fa fa-gamepad"></i>Activity</a>
            </li>
            <li>
              <a href="calendar_page.php">
                <i class="fas fa-star"></i>Event</a>
            </li>
            <li>
              <a href="chatlog_page.php">
                <i class="fa fa-comment"></i>Chat Log</a>
            </li>
            <li>
              <a href="helplog_page.php">
                <i class="fa fa-comment"></i>Help Log</a>
            </li>
            <li>
              <a href="botlog_page.php">
                <i class="fa fa-comment"></i>Bot PM Log</a>
            </li>
            <li>
              <a href="calendar_page.php">
                <i class="fas fa-calendar-alt"></i>Calendar</a>
            </li>
          </ul>
        </div>
      </nav>
    </header>
    <!-- END HEADER MOBILE-->

    <!-- MENU SIDEBAR-->
    <aside class="menu-sidebar d-none d-lg-block">
      <div class="logo">
        <a href="#">
          <img src="images/icon/logo.png" alt="Cool Admin" />
        </a>
      </div>
      <div class="menu-sidebar__content js-scrollbar1">
        <nav class="navbar-sidebar">
          <ul class="list-unstyled navbar__list">
            <li>
              <a href="index_page.php">
                <i class="fas fa-tachometer-alt"></i>Dashboard</a>
            </li>
            <li>
              <a href="activityList_page.php">
                <i class="fa fa-gamepad"></i>Activity</a>
            </li>
            <li>
              <a href="event_page.php">
                <i class="fas fa-star"></i>Event</a>
            </li>
            <li>
              <a href="chatlog_page.php">
                <i class="fa fa-comment"></i>Chat Log</a>
            </li>
            <li>
              <a href="helplog_page.php">
                <i class="fa fa-comment"></i>Help Log</a>
            </li>
            <li>
              <a href="botlog_page.php">
                <i class="fa fa-comment"></i>Bot PM Log</a>
            </li>
            <li>
              <a href="calendar_page.php">
                <i class="fas fa-calendar-alt"></i>Calendar</a>
            </li>
          </ul>
        </nav>
      </div>
    </aside>
    <!-- END MENU SIDEBAR-->

    <!-- PAGE CONTAINER-->
    <div class="page-container">
      <!-- HEADER DESKTOP-->
      <header class="header-desktop">
        <div class="section__content section__content--p30">
          <div class="container-fluid">
            <div class="header-wrap">
              <form class="form-header" action="event_page.php" method="POST">
                <input class="au-input au-input--xl" type="text" name="searchEvent" id="searchEvent" placeholder="Search for event..." />
                <button class="au-btn--submit" type="submit">
                  <i class="zmdi zmdi-search"></i>
                </button>
              </form>
              <div class="header-button">
                <div class="account-wrap">
                  <div class="account-item clearfix js-item-menu">
                    <div class="image">
                      <img src="images/icon/person.png" />
                    </div>
                    <div class="content">
                      <a class="js-acc-btn" href="#"><?php echo $_COOKIE['username'] ?></a>
                    </div>
                    <div class="account-dropdown js-dropdown">
                      <div class="info clearfix">
                        <div class="image">
                          <a href="#">
                            <img src="images/icon/person.png" />
                          </a>
                        </div>
                        <div class="content">
                          <h5 class="name">
                            <a href="#"><?php echo $_COOKIE['username'] ?></a>
                          </h5>
                          <span class="email"><?php echo $_COOKIE['email'] ?></span>
                        </div>
                      </div>
                      <div class="account-dropdown__body">
                        <div class="account-dropdown__item">
                          <a href="account_page.php">
                            <i class="zmdi zmdi-account"></i>Account</a>
                        </div>
                      </div>
                      <div class="account-dropdown__footer">
                        <a href="logout.php"> <i class="zmdi zmdi-power"></i>Logout</a>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </header>
      <!-- END HEADER DESKTOP-->

      <!-- MAIN CONTENT-->
      <div class="main-content">
        <div class="section__content section__content--p30">
          <div class="container-fluid">
            <?php
            if (isset($_GET['erro'])) { ?>
              <p style="color: red; text-align: center"> <?php echo $_GET['erro']; ?></p>
            <?php } ?>
            <?php
            if (isset($_GET['succ'])) { ?>
              <p style="color: green; text-align: center"> <?php echo $_GET['succ']; ?></p>
            <?php } ?>
            <?php
            include 'dbconfig.php';

            $dbconn = pg_connect("host=$dbhost dbname=$dbname user=$dbuser password=$dbpass")
              or die('Could not connect: ' . pg_last_error());

            $query = pg_query($dbconn, 'SELECT COUNT(*) FROM Activity');

            $rowCount = intval(pg_fetch_result($query, 0, 0));

            if ($rowCount != 0) {
              echo '<div align="right">';
              echo '<a class="btn btn-primary" href="newEvent_page.php">';
              echo '<i class="fa fa-star"></i>&nbsp; NEW</a>';
              echo '</div>';
            }
            ?>

            <div class="row">
              <div class="table-responsive table-responsive-data2">
                <table class="table table-data2">
                  <thead>
                    <tr>
                      <th>name</th>
                      <th>description</th>
                      <th>date</th>
                      <th>Submission Deadline</th>
                      <th>Maximum number of member</th>
                      <th></th>
                    </tr>
                  </thead>
                  <?php
                  if (isset($_POST['searchEvent'])) {
                    require 'getEvent.php';
                    echo searchEventByKey($_POST['searchEvent']);
                  } else {
                    include('getAllEvent.php');
                  }
                  ?>
                </table>
              </div>
              <div class="row" style="width: 100%">
                <div class="col-md-12">
                  <div class="copyright">
                    <p>
                      Copyright © 2018 Colorlib. All rights reserved. Template
                      by <a href="https://colorlib.com">Colorlib</a>.
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Jquery JS-->
    <script src="vendor/jquery-3.2.1.min.js"></script>
    <!-- Bootstrap JS-->
    <script src="vendor/bootstrap-4.1/popper.min.js"></script>
    <script src="vendor/bootstrap-4.1/bootstrap.min.js"></script>
    <!-- Vendor JS       -->
    <script src="vendor/slick/slick.min.js"></script>
    <script src="vendor/wow/wow.min.js"></script>
    <script src="vendor/animsition/animsition.min.js"></script>
    <script src="vendor/bootstrap-progressbar/bootstrap-progressbar.min.js"></script>
    <script src="vendor/counter-up/jquery.waypoints.min.js"></script>
    <script src="vendor/counter-up/jquery.counterup.min.js"></script>
    <script src="vendor/circle-progress/circle-progress.min.js"></script>
    <script src="vendor/perfect-scrollbar/perfect-scrollbar.js"></script>
    <script src="vendor/chartjs/Chart.bundle.min.js"></script>
    <script src="vendor/select2/select2.min.js"></script>

    <!-- full calendar requires moment along jquery which is included above -->
    <script src="vendor/fullcalendar-3.10.0/lib/moment.min.js"></script>
    <script src="vendor/fullcalendar-3.10.0/fullcalendar.js"></script>

    <!-- Main JS-->
    <script src="js/main.js"></script>

</body>

</html>
<!-- end document-->