<?php
function submit_status($data, $author) {
    $fp = fopen("../xml/diary.html", "a");
    if ($data) {
        if (is_null($author))
            $author = 'null';
        if (fwrite($fp, '<p>' . date('Y-m-d H:i:s') . '<br/>' . $data . '<br/>by <b>' . $author . '</b></p>' . "\n")) {
            echo "<p><b>success</b></p>";
        }
        else
            echo "<p><b>fail</b></p>";
    }
    fclose($fp);
}

$code = '123';

$log_file = fopen("../xml/log.txt", "a");
fwrite($log_file, date('Y-m-d H:i:s') . ' from ' . $_SERVER["REMOTE_ADDR"] . " port:" . $_SERVER['REMOTE_PORT'] . "\n");
fclose($log_file);
?>
<html>
    <head>
        <meta charset="utf-8">
        <link rel="stylesheet" type="text/css" href="/css/bootstrap.css">
        <link rel="stylesheet" type="text/css" href="/css/diary.css">
        <title>Write down your heart❤</title>
        <script type="text/javascript" src="/js/jquery.js"></script>
        <script type="text/javascript" src="/js/bootstrap.js"></script>
        <script type="text/javascript" src="/js/diary.js"></script>
    </head>

    <body>
        <div class="container">
            <div class="row">
                <form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>">
                    <p class="title">Today<b>(<?php echo date('Y-m-d l');?>)</b>'s words:</p>
                    <textarea name="content" rows="10" cols="100"></textarea>
                    <p class="author">Author: 
                    <input type="radio" name="author" value="Liubaobao"/>Liubaobao
                    <input type="radio" name="author" value="Tantan">Tantan
                    </p>
                    <input type="submit" value="Send" class="btn-primary submit"/>
                </form>
                <button class="btn-info view">view previous diaries</button>
            </div>
            <br/>
            <div class="row">
            <?php submit_status($_POST['content'], $_POST['author']);?>
            </div>
            <div class="row" id="invisible">
                <form method="post" action="<?php echo htmlspecialchars($_SERVER['PHP_SELF']);?>">
                    Code: <input type="password" name="code"/>
                    <input type="submit" value="verify"/>
                </form>
            </div>
            <br/>
            <div class="row">
                <?php
                if (!is_null($_POST['code'])) {
                    if ($_POST['code'] === $code) {
                        $fr = fopen("../xml/diary.html", 'r');
                        echo fread($fr, filesize("../xml/diary.html"));
                        fclose($fr);
                    }
                    else {echo "Code wrong!<br/>Ask Jiashuo Liu for more infomation...";}
                }
                ?>
            </div>
        </div>
    </body>
</html>