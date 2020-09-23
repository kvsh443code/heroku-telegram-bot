<?php
echo "
<!DOCTYPE HTML>
<html lang="en">
  <head>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  </head>
  <body>
    <h1> HEROKU PHP DEPLOY </h1>
      <b> ごめんなさい </b>
      <br/>
      <b> UnU ! I had to make data public to get these data to Power BI for analysis</b>
      <br/>
      <br/>
      <div class = "container"> 
";


$conn = pg_connect("dbname=dfl8q695f86rlm host=ec2-3-224-97-209.compute-1.amazonaws.com port=5432 user=rzgeksqnykwxll password=443be8c4cbac281b8f026e95db5f86e439c608ccf4b296310b88effb736f8463 sslmode=require");
$result = pg_query($conn, "SELECT * FROM msg");
echo "<table border=1> <tr><th>ID</th><th>CHAT ID</th><th>MESSAGE</th><th>DATE & Time</th><th>STATUS</th></tr>";
while ($row = pg_fetch_assoc($result)) {
  echo "<tr><td>" .$row['id']. "</td>
            <td>" .$row['chat_id']. "</td>
            <td>" .$row['message']. "</td>
            <td>" .$row['date_time']. "</td>
            <td>" .$row['status']. "</td>
        </tr>\n";
}

echo "
</table>
    </div>
</body>
</html>";
?>
