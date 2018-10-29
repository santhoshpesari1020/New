<html>
<body>
<h2>Hello World! Hello Welcome to my world</h2>
  
var userposition=location.href.indexOf("user=");
var user=location.href.substring(userposition+5);
document.getElementById("Welcome").innerHTML=" Hello, "+user;


</body>
</html>
