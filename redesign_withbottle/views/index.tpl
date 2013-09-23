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
    <script src="bootstrap.min.js"></script>

    <!-- HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
      <script src="assets/js/html5shiv.js"></script>
    <![endif]-->

    <!-- Fav and touch icons -->
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="assets/ico/apple-touch-icon-144-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="../assets/ico/apple-touch-icon-114-precomposed.png">
      <link rel="apple-touch-icon-precomposed" sizes="72x72" href="../assets/ico/apple-touch-icon-72-precomposed.png">
      <link rel="apple-touch-icon-precomposed" href="../assets/ico/apple-touch-icon-57-precomposed.png">
      <link rel="shortcut icon" href="../assets/ico/favicon.png">
  
  %include('css.tpl')

  </head>

  <body>

    % include('navbar.tpl')
    <div class="container-fluid">
      <div class="row-fluid">
        <div class="span3">
        % include('sidebar.tpl')
        </div>
        <div class="span9">
          %include('carousel.tpl')
        
          <div class="row-fluid">
            %include('features.tpl')
          </div><!--/row-->

        </div><!--/span 9-->
      </div><!--/row-->
      
      <hr>
      
      <footer>
        %include('footer.tpl')
      </footer>

    </div><!--/.fluid-container-->

    <!-- Le javascript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="bootstrap.min.js"></script>
    
    <!--- Carousel JQuery -->
    <script>
    $(document).ready(function(){
     $('#head-carousel-001').carousel();
    });
    </script>
  
  </body>
</html>
