<?php
$serv_port = 8001;
$serv_ip = '192.168.1.159';
$sock_out = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
socket_bind($sock_out, $serv_ip, $serv_port);
socket_listen($sock_out, 5);
$sock_in = socket_accept($sock_out);
$con = socket_connect($sock_out, $serv_ip, $serv_port);
if (!$con) {
    echo "socket_connect() failed.<br/>Reason: " . socket_strerror(socket_last_error($sock_out));
} else {
    echo "OK<br/>";
}

$reply = '';
if (!empty($_POST['content'])) {
    $cmd = $_POST['content'];
    if ($cmd === "窗帘") {
        $msg = "1 " + $_POST['state'];
        socket_write($sock_out, $msg, strlen($msg));
    } else if ($cmd === "风扇") {
        $msg = "2 " + $_POST['state'];
        socket_write($sock_out, $msg, strlen($msg));
    } else if ($cmd === "电灯") {
        $msg = "3 " + $_POST['state'];
        socket_write($sock_out, $msg, strlen($msg));
    } else if ($cmd === "插座") {
        $msg = "4 " + $_POST['state'];
        socket_write($sock_out, $msg, strlen($msg));
    } else if ($cmd === "温湿度") {
        $msg = "5 0";
        socket_write($sock_out, $msg, strlen($msg));
        $reply = socket_read($sock_out, 1024);
    } else if ($cmd === "烟雾") {
        $msg = "6 0";
        socket_write($sock_out, $msg, strlen($msg));
        $reply = socket_read($sock_out, 1024);
    }
}
?>
<form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>">
    <p>command:</p>
    <textarea name="content" rows="10" cols="100"></textarea>
    <p>state:</p>
    <input type="radio" name="state" value="1">open
    <input type="radio" name="state" value="0">close
    <br/><br/>
    <input type="submit" value="confirm">
</form>
<?php
if (!empty($reply)) {
    echo "<br/>";
    echo $cmd . ': ' . $reply;
}
?>
