<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Davis CS Club</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">
    <!-- Fonts -->
    <link href='http://fonts.googleapis.com/css?family=Gudea:400,700|Roboto+Slab' rel='stylesheet' type='text/css'>
    <!-- Le styles -->
    
    <!--- Carousel JQuery -->
    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
    <script>window.jQuery || document.write('<script src="js/jquery-1.7.2.min.js"><\/script>')</script>
    <script src="static/js/bootstrap.min.js"></script>

    <!-- HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
      <script src="static/js/html5shiv.js"></script>
    <![endif]-->

    <!-- Fav and touch icons -->
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="static/ico/apple-touch-icon-144-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="../static/ico/apple-touch-icon-114-precomposed.png">
      <link rel="apple-touch-icon-precomposed" sizes="72x72" href="../static/ico/apple-touch-icon-72-precomposed.png">
      <link rel="apple-touch-icon-precomposed" href="../static/ico/apple-touch-icon-57-precomposed.png">
      <link rel="shortcut icon" href="../static/ico/favicon.png">
  
  <link href="static/css/bootstrap.css" rel="stylesheet">
  <style type="text/css">
    body {
      padding-top: 60px;
      padding-bottom: 40px;
    }
  </style>
  <link href="static/css/bootstrap-responsive.css" rel="stylesheet">
  <link href="static/webfonts/fonts.css" rel="stylesheet">
  <link href="static/css/style.css" rel="stylesheet">

  </head>

  <body>
    <div class="container">
    <div class="navbar navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <a class="brand" href="#">Davis CS Club</a>
          <div class="nav-collapse collapse">
            
              <ul class="nav pull-right">
                <li class="active">
                  <a href="#">Home</a>
                </li>
                
              </ul>
          
          </div><!--/.nav-collapse -->
        </div>
      </div>
    </div>

    <div class="container-fluid">
      <div class="row-fluid">
        <div class="span3">
          <div class="sidebar-nav">
            <img src="static/images/title.png" />
            <ul class="nav nav-list">
              <p class="lead">hello! we are aggies who love technology, beautiful code, and good design.</p>
              
              <li class="nav-header">Upcoming Events</li>
              <li>
                <img src="static/images/events/cat.jpg" /> 
                <span class="eventtitle"> Welcome Freshmen & Transfers! </span>
                <p> Sept 30, 2013 (Mon) <br /> 5:30pm - 6:30pm <br /> TCS Building Room 107 <br />
                  <a href="http://campusmap.ucdavis.edu/?b=21">(click here for map)</a>
              </li>
              <li>
                <img src="static/images/events/pragmatic.jpg" /> 
                <span class="eventtitle"> Pragmatic Programming Committee - First Meeting</span>
                <p> Oct 10, 2013 (Thurs) <br /> 3:00pm - 4:00pm <br /> TBA
              </li>
            </ul>
          </div><!--/.well -->
        </div><!--/span-->
        <div class="span9">
         
          <!--  Carousel - consult the Twitter Bootstrap docs at
                http://twitter.github.com/bootstrap/javascript.html#carousel -->
          <div id="head-carousel-001" class="carousel slide"><!-- class of slide for animation -->
            <div class="carousel-inner">
              <div class="item active"><!-- class of active since it's the first item -->
                <img src="static/images/carousel/welcome-carousel.png" alt="" />
                <div class="carousel-caption">
                  <p class="carousel-title">Join us for our New Student Welcome Event!</p>
                  <p>Sept 30, 2013 at 5:30pm - 6:30pm, TCS Building Room 107 
                    <a href="http://campusmap.ucdavis.edu/?b=21">(click here for map)</a>
                  </p>
                </div>
              </div>
              <div class="item">
                <img src="static/images/carousel/meeting.png" alt="" />
                <div class="carousel-caption">
                  <p class="carousel-title">Learn, play, and get to know everyone.</p>
                  <p>Look out for our next events!</p>
                </div>
              </div>
              <div class="item">
                <img src="static/images/carousel/welikepizza.png" alt="" />
                <div class="carousel-caption">
                  <p class="carousel-title">We like pizza! Do you?</p>
                  <p>We almost always have food in our events. :D</p>
                </div>
              </div>
            </div><!-- /.carousel-inner -->
            <!--  Next and Previous controls below
                  href values must reference the id for this carousel -->
              <a class="carousel-control left" href="#head-carousel-001" data-slide="prev">&lsaquo;</a>
              <a class="carousel-control right" href="#head-carousel-001" data-slide="next">&rsaquo;</a>
          </div><!-- /.carousel -->
          <div class="row-fluid">
            <div class="span4">
              <img src="static/images/features/prag.jpg" />
              <h2>Pragmatic Programming</h2>
              <p>Chair: Aria Sabeti <br />
                 This group aims to help make everyone be better programmers. They tackle mind-bending programming puzzles to sharpen problem solving skills, and talk about what makes code beautiful.
              </p>
              <!--<p><a class="btn" href="#">More &raquo;</a></p>-->
            </div><!--/span-->
            <div class="span4">
              <img src="static/images/features/meeting.png" />
              <h2>Professional Development</h2>
              <p>Chair: Kevin Liu <br />
                 This committee helps club members develop a professional network. We help you build your resume, host community coding events, discover interships, and bring about other opportunities.
              </p>
              <!--<p><a class="btn" href="#">More &raquo;</a></p>-->
            </div><!--/span-->
            <div class="span4">
              <img src="static/images/features/teach.png" />
              <h2>Tutoring</h2>
              <p>Chair: Rajan Singh <br />
                 We're all students, and sometimes, classes get tough, so this group is here to help. Armed with their knowledge and their passion for teaching, the tutoring committee will help keep your stress levels down and your grades high.
              </p>
              <!--<p><a class="btn" href="#">More &raquo;</a></p>-->
            </div><!--/span-->
          </div><!--/row-->
      
         

        </div><!--/big span 9-->
      </div><!--/row-->
      
      <hr>

      <footer>
        <div class="container"> 
             
          <div class="row-fluid">
            
            <div class="span2">
              <img src="static/images/signup2.png" />
            </div>

            <div class="span6">
              <form id="newsletter" action="/" method="post">          
                <input type="text" name="name" placeholder="Name" /> <br />
                <input type="text" name="email" placeholder="UC Davis e-mail" /> 
                <br />
                %if error_msg is not None:
                <h3>{{error_msg}}</h3>
                %elif submit is True:
                <h3>Woo hoo, you are now registered! Look out for
                newsletters ahead!</h3>
                %else:
                <input type="submit" value="Submit" />
                %end 
                <!-- 

                replace above button with this button for a success notification:
                
                <input type="submit" class="btn-success" disabled="disabled" value="Success! [put email here] has been added."/ 
                
                (side note: disabled="disabled" is actually how html disables an input tag of type "submit". what.)

                -->
              </form> 
              
            </div>
            <div class="span4">
              <a href="https://www.facebook.com/groups/daviscsclub/">
                <img src="static/images/social/facebook.png" class="social"/>
              </a>
              <a href="https://twitter.com/TheDavisCSClub">
                <img src="static/images/social/twitter.png" class="social"/>
              </a>
              <a href="#">
                <img src="static/images/social/email.png" class="social"/>
              </a>
            </div>    
                    
          </div>
           <p class="muted pull-right">&copy; 2013 Davis CS Club. All rights reserved</p>
          </div>
      </footer>

    </div><!--/.fluid-container-->

    <!-- Le javascript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="static/js/bootstrap.min.js"></script>
    

      <!--- Carousel JQuery -->

      <script>
      $(document).ready(function(){
       $('#head-carousel-001').carousel();
      });
      </script>

  </div>
  </body>
</html>
