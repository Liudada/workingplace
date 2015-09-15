<?php
$icderror = $usnerror = $pwderror = "";
$icd = $usn = $pwd = "";

$con = mysql_connect('localhost', 'root', 'qazwsxedc');
if (!$con) {
    die('Could not connect: ' . mysql_error());
}
mysql_select_db("mydb", $con);

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (empty($_POST['icd'])) {
        $icderror = "invitation code required";
    } else {
        $icd = test_input($_POST['icd']);
        $validicd = mysql_query("select * from InvCode where code='" . $icd . "';");
        $row = mysql_fetch_array($validicd);
        if (empty($row)) {
            $icderror = "invitation code not in database";
        } else {
            $id = $row['id'];
            $validicd = mysql_query("select * from UserCode where id='" . $id . "';");
            $row = mysql_fetch_array($validicd);
            if (!empty($validicd)) {
                $icderror = "invitation code used";
            }
        }
    }

    if (empty($_POST['usn'])) {
        $usnerror = "valid username required";
    } else {
        $usn = test_input($_POST['usn']);
        $validusn = mysql_query("select * from UserCode where usr='" . $usn . "';");
        $row = mysql_fetch_array($validusn);
        if (empty($row)) {
            mysql_query("insert into UserCode values (" . $id . ",'" . $_POST['pwd'] . "','" . $_POST['usn'] . "');");
        } else {
            $usnerror = "username already used";
        }
    }

    if (empty($_POST['pwd'])) {
        $pwderror = "password required";
    } else {
        $pwd = test_input($_POST['pwd']);
        if (strlen($pwd) < 6) {
            $pwderror = "password should be longer than 6 bytes";
        }
    }
}

function test_input($data) {
    $data = trim($data);
    $data = stripcslashes($data);
    $data = htmlspecialchars($data);
    return $data;
}

mysql_close();
?>

<html>
    <head>
        <script src="test.js"></script>
        <style type="text/css">
            .error {color: #ff0000;}
        </style>
    </head>
    <body>
        <div id="invite">
            <form action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>" method="POST">
                Invitation Code: <input type="text" name="icd"><span class="error"> * <?php echo $icderror;?></span><br/>
                UserName: <input type="text" name="usn"><span class="error"> * <?php echo $usnerror;?></span><br/>
                Password: <input type="password" name="pwd"><span class="error"> * <?php echo $pwderror;?></span><br/>
                <input type="submit" value="submit">
            </form>
        </div>
    </body>
</html>