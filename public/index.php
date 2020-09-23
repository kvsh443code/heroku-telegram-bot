<?php
echo "
<!DOCTYPE HTML>
<html>
  <body>
    <h1> HEROKU PHP DEPLOY </h1>
      <b> UwU </b>
      <br/>
      <b> OwO </b>
      <br/>
      <br/>";


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
</body>
</html>";
?>
