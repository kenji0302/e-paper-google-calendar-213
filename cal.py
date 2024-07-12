import network
import time
import ujson
import urequests

def jst_ymd():
    """JSTのymdを取得する

    Returns:
        string : yyyymmdd
    """
    utctime = time.localtime()
    JST_OFFSET = 9 * 60 * 60
    jst_time = time.localtime(time.mktime(utctime) + JST_OFFSET)
    return "{:04d}{:02d}{:02d}".format(jst_time[0], jst_time[1], jst_time[2])

def jst_today_ymdhms_for_api():
    """APIリクエスト用のJSTのymdhmsを取得する

    Returns:
        string : yyyy-mm-ddT00:00:00Z
    """
    utctime = time.localtime()
    JST_OFFSET = 9 * 60 * 60
    jst_time = time.localtime(time.mktime(utctime) + JST_OFFSET)
    
    return "{:04d}-{:02d}-{:02d}T00:00:00Z".format(jst_time[0], jst_time[1], jst_time[2])

def wifi_connect(ssid, password):
    """Wifiに接続する

    Args:
        ssid (string): ssid
        password (string): パスワード
    """
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    print("Connecting to WiFi")

    while not wlan.isconnected():
        print(".")
        time.sleep(1)
    print("Connected")
    wlan_status = wlan.ifconfig()
    print(f'IP Address: {wlan_status[0]}')
    
    return wlan
    

def refresh_access_token(client_id, client_secret, refresh_token):
    """ oauthのアクセストークンをリフレッシュ

    """
    token_url = 'https://oauth2.googleapis.com/token'
    payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'refresh_token': refresh_token,
        'grant_type': 'refresh_token'
    }
    
    response = urequests.post(token_url, data=ujson.dumps(payload), headers={'Content-Type': 'application/json'})
    tokens = response.json()
    print(tokens)
    new_access_token = tokens.get('access_token')
    return new_access_token


def jpredchar(fd, epd, x, y, width, height):
    bn = (width+7)>>3
    py = y
    for i in range(0, len(fd), bn):
        px = x
        for j in range(bn):
            for k in range(8 if (j+1)*8 <=width else width % 8):
                if fd[i+j] & 0x80>>k:
                    epd.imagered.pixel(px + k, py, 0x00)
            px+=8
        py+=1


def jpblackchar(fd, epd, x, y, width, height): 
    bn = (width+7)>>3
    py = y
    for i in range(0, len(fd), bn):
        px = x
        for j in range(bn):
            for k in range(8 if (j+1)*8 <=width else width % 8):
                if fd[i+j] & 0x80>>k:
                    epd.imageblack.pixel(px + k, py, 0x00)
            px+=8
        py+=1


def jpredtext(str, x, y, mf, epd):
    mf.begin()
    for c in str:
        d = mf.getFont(ord(c))
        jpredchar(d, epd, x, y, mf.getWidth(), mf.getHeight())
        x = x + mf.getWidth()
    mf.end()

def jpblacktext(str, x, y, mf, epd):
    mf.begin()
    for c in str:
        d = mf.getFont(ord(c))
        jpblackchar(d, epd, x, y, mf.getWidth(), mf.getHeight())
        x = x + mf.getWidth() 
    mf.end()


