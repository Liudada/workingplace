<?php
//traceHttp();
//enable this function to record incoming ip

define("TOKEN", "testing");         //same token on weixin platform
$wechatObj = new wechatCallbackapiTest();
if (isset($_GET['echostr'])) {
    $wechatObj->valid();            //fail frequently, try some other times
} else {
    $wechatObj->responseMsg();
}

class wechatCallbackapiTest
{
    public function valid()
    {
        $echoStr = $_GET["echostr"];
        if($this->checkSignature()){
            echo $echoStr;
            exit;
        }
    }

    private function checkSignature()
    {
        $signature = $_GET["signature"];
        $timestamp = $_GET["timestamp"];
        $nonce = $_GET["nonce"];
        $token = TOKEN;
        $tmpArr = array($token, $timestamp, $nonce);
        sort($tmpArr);
        $tmpStr = implode( $tmpArr );
        $tmpStr = sha1( $tmpStr );

        if( $tmpStr == $signature ){
            return true;
        }else{
            return false;
        }
    }

    public function responseMsg()
    {
        $serv_port = 51706;                     //configurations
        $serv_ip = '166.111.198.30';
        $sock_out = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
        $postStr = $GLOBALS["HTTP_RAW_POST_DATA"];
        if (!empty($postStr)){
            $postObj = simplexml_load_string($postStr, 'SimpleXMLElement', LIBXML_NOCDATA);
            $fromUsername = $postObj->FromUserName;
            $toUsername = $postObj->ToUserName;
            $keyword = trim($postObj->Content);
            $time = time();
            $textTpl = "<xml>
                        <ToUserName><![CDATA[%s]]></ToUserName>
                        <FromUserName><![CDATA[%s]]></FromUserName>
                        <CreateTime>%s</CreateTime>
                        <MsgType><![CDATA[%s]]></MsgType>
                        <Content><![CDATA[%s]]></Content>
                        <FuncFlag>0
                        </FuncFlag>
                        </xml>";
            $con = socket_connect($sock_out, $serv_ip, $serv_port);
            if ($con === false) {
                $errmsg = "socket_connect() failed.<br/>Reason: " . socket_strerror(socket_last_error($sock_out));
                echo $errmsg;
            } else {$msg = "test";}
            if (!empty($keyword))
            {
                sscanf($keyword, "%s", $cmd);           //this part can be better programmed by calling a function.
                if ($cmd === "温度" || $cmd === "温度。")
                    $msg = "701";
                elseif ($cmd === "窗帘" || $cmd === "窗帘。")
                    $msg = "101";
                elseif ($cmd === "液晶" || $cmd === "液晶。")
                    $msg = "201";
                elseif ($cmd === "开启窗帘" || $cmd === "开启窗帘。")
                    $msg = "110";
                elseif ($cmd === "关闭窗帘" || $cmd === "关闭窗帘。")
                    $msg = "100";
                elseif ($cmd === "开启液晶" || $cmd === "开启液晶。")
                    $msg = "210";
                elseif ($cmd === "关闭液晶" || $cmd === "关闭液晶。")
                    $msg = "200";
                elseif ($cmd === "全部" || $cmd === "全部。")
                    $msg = "800";
                socket_write($sock_out, $msg, strlen($msg));
                if ($msg === "800") {
                    //can be promoted
                    $reply1 = socket_read($sock_out, 1024);
                    $reply2 = socket_read($sock_out, 1024);
                    $reply3 = socket_read($sock_out, 1024);
                    $reply = $reply1;
                    $num = substr($reply, 0, 1);
                    $state = substr($reply, 1, 1);
                    if ($num === "1")
                        $num = "窗帘";
                    elseif ($num === "2")
                        $num = "液晶屏幕";
                    elseif ($num === "7") {
                        $num = "温度";
                        $state = substr($reply, 1, 2) . "摄氏度";
                    }
                    else
                        $num = "设备unknown";
                    if ($num !== "温度") {
                        if ($state === "1")
                            $state = "开启";
                        elseif ($state === "0")
                            $state = "关闭";
                        else
                            $state = "Unknown";
                    }
                    $msg1 = $num . " " . $state;
                    $reply = $reply2;
                    $num = substr($reply, 0, 1);
                    $state = substr($reply, 1, 1);
                    if ($num === "1")
                        $num = "窗帘";
                    elseif ($num === "2")
                        $num = "液晶屏幕";
                    elseif ($num === "7") {
                        $num = "温度";
                        $state = substr($reply, 1, 2) . "摄氏度";
                    }
                    else
                        $num = "设备unknown";
                    if ($num !== "温度") {
                        if ($state === "1")
                            $state = "开启";
                        elseif ($state === "0")
                            $state = "关闭";
                        else
                            $state = "Unknown";
                    }
                    $msg2 = $num . " " . $state;
                    $reply = $reply3;
                    $num = substr($reply, 0, 1);
                    $state = substr($reply, 1, 1);
                    if ($num === "1")
                        $num = "窗帘";
                    elseif ($num === "2")
                        $num = "液晶屏幕";
                    elseif ($num === "7") {
                        $num = "温度";
                        $state = substr($reply, 1, 2) . "摄氏度";
                    }
                    else
                        $num = "设备unknown";
                    if ($num !== "温度") {
                        if ($state === "1")
                            $state = "开启";
                        elseif ($state === "0")
                            $state = "关闭";
                        else
                            $state = "Unknown";
                    }
                    $msg3 = $num . " " . $state;
                    $msg = $msg1 . "\n" . $msg2 . "\n" . $msg3;
                } else {
                    $reply = socket_read($sock_out, 1024);
                    $num = substr($reply, 0, 1);
                    $state = substr($reply, 1, 1);
                    if ($num === "1")
                        $num = "窗帘";
                    elseif ($num === "2")
                        $num = "液晶屏幕";
                    elseif ($num === "7") {
                        $num = "温度";
                        $state = substr($reply, 1, 2) . "摄氏度";
                    }
                    else
                        $num = "设备unknown";
                    if ($num !== "温度") {
                        if ($state === "1")
                            $state = "开启";
                        elseif ($state === "0")
                            $state = "关闭";
                        else
                            $state = "Unknown";
                    }
                    $msg = $num . " " . $state;
                }
                $msgType = "text";
                $resultStr = sprintf($textTpl, $fromUsername, $toUsername, $time, $msgType, $msg);
                echo $resultStr;
                socket_close($sock_out);
            } else {
                $msgType = "text";
                $resultStr = sprintf($textTpl, $fromUsername, $toUsername, $time, $msgType, $msg);
                echo $resultStr;
            }
        } else {
            $msgType = "text";
            $resultStr = sprintf($textTpl, $fromUsername, $toUsername, $time, $msgType, $msg);
            echo $resultStr;
        }
    }
}

function traceHttp()
{
    logger("\n\nREMOTE_ADDR:".$_SERVER["REMOTE_ADDR"].(strstr($_SERVER["REMOTE_ADDR"],'101.226')? " FROM WeiXin": "Unknown IP"));
    logger("QUERY_STRING:".$_SERVER["QUERY_STRING"]);
}
function logger($log_content)
{
    if(isset($_SERVER['HTTP_APPNAME'])){   //SAE
        sae_set_display_errors(false);
        sae_debug($log_content);
        sae_set_display_errors(true);
    }else{ //LOCAL
        $max_size = 500000;
        $log_filename = "log.xml";
        if(file_exists($log_filename) and (abs(filesize($log_filename)) > $max_size)){unlink($log_filename);}
        file_put_contents($log_filename, date('Y-m-d H:i:s').$log_content."\r\n", FILE_APPEND);
    }
}
?>