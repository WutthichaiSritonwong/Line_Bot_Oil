from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import requests

app = Flask(__name__)

line_bot_api = LineBotApi('QN01ycDGxaiS1HGsfVecKp+K9OEWp55wV+Vb5t37JSPh2VouGorNBZhR+lpCucZtTXiUViFJCnjsH9rotOU3E+a5rP+W8Dsd45WiPpXSvT3VPWh7Q0exotCCp/qua9byp7eg3AyNl4NteMYU6WFPtgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('b79ea5129d92d6b867458805cefe29d0')

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == 'ptt':
        # json_data = requests.get('https://api.chnwt.dev/thai-oil-api/latest').json()
        url = 'https://api.chnwt.dev/thai-oil-api/latest'
        res = requests.get(url)

        data = res.json()
        ptt = data['response']['stations']['ptt']
        date = data['response']['date']
        gasoline_95 = ptt['gasoline_95']['name'] + ' ราคา: '+ ptt['gasoline_95']['price'] + ' บาท'
        gasohol_95 = ptt['gasohol_95']['name'] + ' ราคา: '+ ptt['gasohol_95']['price'] + ' บาท'
        gasohol_91 = ptt['gasohol_91']['name'] + ' ราคา: '+ ptt['gasohol_91']['price'] + ' บาท'
        gasohol_e20 = ptt['gasohol_e20']['name'] + ' ราคา: '+ ptt['gasohol_e20']['price'] + ' บาท'
        gasohol_e85 = ptt['gasohol_e85']['name'] + ' ราคา: '+ ptt['gasohol_e85']['price'] + ' บาท'
        diesel = ptt['diesel']['name'] + ' ราคา: '+ ptt['diesel']['price'] + ' บาท'
        diesel_b7 = ptt['diesel_b7']['name'] + ' ราคา: '+ ptt['diesel_b7']['price'] + ' บาท'
        diesel_b20 = ptt['diesel_b20']['name'] + ' ราคา: '+ ptt['diesel_b20']['price'] + ' บาท'
        premium_diesel = ptt['premium_diesel']['name'] + ' ราคา: '+ ptt['premium_diesel']['price'] + ' บาท'
        premium_gasohol_95 = ptt['premium_gasohol_95']['name'] + ' ราคา: '+ ptt['premium_gasohol_95']['price'] + ' บาท'
        superpower_gasohol_95 = ptt['superpower_gasohol_95']['name'] + ' ราคา: '+ ptt['superpower_gasohol_95']['price'] + ' บาท'
        json_data = gasoline_95,gasohol_95,gasohol_91,gasohol_e20,gasohol_e85,diesel,diesel_b7,diesel_b20,premium_diesel,premium_gasohol_95,superpower_gasohol_95
        # ทำการจัดรูปแบบข้อมูล JSON ตามที่คุณต้องการ
        # ยังสามารถทำการวนลูปข้อมูลและส่งข้อมูลกลับไปยัง LINE
        response = f"ราคาน้ำมัน Update : {date}\n"
        # for key, value in json_data.items():
        #     response += f"{key}: {value}\n"
        for i in json_data:
            response += f"{i}\n"

        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=response)
        )

if __name__ == "__main__":
    app.run()