import urequests
import ntptime
import urequests
from cal import jst_ymd, wifi_connect, refresh_access_token, jpredtext, jpblacktext, jst_today_ymdhms_for_api
from EPD_2in13_B_V4_Portrait import EPD_2in13_B_V4_Landscape
from mfont import mfont
from secret import WIFI_SSID, WIFI_PASSWORD,GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, GOOGLE_REFRESH_TOKEN,GOOGLE_CALENDAR_ID

if __name__=='__main__':
    
    while True:

        machine.Pin(23, machine.Pin.OUT).high()

        # Wifi接続
        wlan = wifi_connect(WIFI_SSID, WIFI_PASSWORD)
        ntptime.settime()

        # ymd取得
        ymd = jst_ymd()
        # print(ymd)

        # カレンダー取得
        access_token = refresh_access_token(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET, GOOGLE_REFRESH_TOKEN)

        # 画面表示
        epd = EPD_2in13_B_V4_Landscape()
        epd.Clear(0xff, 0xff)
        epd.imageblack.fill(0xff)
        epd.imagered.fill(0xff)


        mf = mfont()
        mf.setFontSize(16)    
        
        # deepsleep 1時間
        sleep_msec = 3600000
        if access_token is None:
            # deepsleep 24時間
            sleep_msec = 86400000
            jpredtext("カレンダーにアクセス出来ません。", 5, 10, mf, epd)
            jpredtext("トークンを更新してください。", 5, 35, mf, epd)
        else:

            calendar_id = "primary"

            ymdhms = jst_today_ymdhms_for_api() 
            
            url = "https://www.googleapis.com/calendar/v3/calendars/" + GOOGLE_CALENDAR_ID + "/events?maxResults=6&timeMin=" + ymdhms + "&orderBy=startTime&singleEvents=True&timeZone=JST"

            headers = {
                "Authorization": "Bearer " + access_token
            }

            response = urequests.get(url, headers=headers)

            if response.status_code == 200:

                events = response.json().get('items', [])            
                
                # 画面表示
                epd = EPD_2in13_B_V4_Landscape()
                epd.Clear(0xff, 0xff)
                epd.imageblack.fill(0xff)
                epd.imagered.fill(0xff)


                mf = mfont()
                mf.setFontSize(16)    

                x = 10
                i = 0
                
                for event in events:
                    if 'date' in event['start']:
                        event_ymd = event['start']['date'][0:4] + event['start']['date'][5:7] + event['start']['date'][8:10]
                        event_str = event['start']['date'][5:7] + '月' + event['start']['date'][8:10] + '日' + ' ' + event['summary']
                        print(event_str)
                    elif 'dateTime' in event['start']:
                        event_ymd = event['start']['dateTime'][0:4] + event['start']['dateTime'][5:7] + event['start']['dateTime'][8:10]
                        event_str = event['start']['dateTime'][5:7] + '月' + event['start']['dateTime'][8:10] + '日' +   event['start']['dateTime'][11:16] + ' ' + event['summary']
                        print(event_str)
                    
                    if event_ymd == ymd:
                        jpredtext(event_str, 5, x, mf, epd)
                    else:
                        jpblacktext(event_str, 5, x, mf, epd)
                    x = x + 25
                    i = i + 1
            else:
                print("Failed to retrieve events:", response.status_code, response.text)


        epd.display()
        
        print("deepsleep")
        
        machine.Pin(23, machine.Pin.OUT).low()
        machine.deepsleep(sleep_msec)
