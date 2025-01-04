<?php
$CLIENT_ID = "クライアントID";
$CLIENT_SECRET = "クライアントシークレット";
$REDIRECT_URI = "http://localhost:8080/";
?>
<html>

<body>
    <p>
        <a href="https://accounts.google.com/o/oauth2/v2/auth?client_id=<?php echo $CLIENT_ID ?>&redirect_uri=<?php echo $REDIRECT_URI ?>&scope=https://www.googleapis.com/auth/calendar.readonly&response_type=code&access_type=offline&prompt=consent">認証</a>
    </p>
    <?php if (!empty($_GET['code'])) { ?>
        <p>

        <form method="post" action="https://www.googleapis.com/oauth2/v4/token">
            <input type="hidden" name="code" value="<?php echo htmlentities($_GET['code']) ?>" />
            <input type="hidden" name="redirect_uri" value="<?php echo htmlentities($REDIRECT_URI) ?>" />
            <input type="hidden" name="client_id" value="<?php echo htmlentities($CLIENT_ID) ?>" />
            <input type="hidden" name="client_secret" value="<?php echo htmlentities($CLIENT_SECRET) ?>" />
            <input type="hidden" name="scope" value="" />
            <input type="hidden" name="grant_type" value="authorization_code" />
            <input type="hidden" name="prompt" value="true" />
            <input type="hidden" name="access_type" value="offline" />
            <input type="submit" name="token取得" />
        </form>
        </p>

    <?php } ?>
</body>

</html>
