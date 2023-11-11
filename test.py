from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import requests
import json

app = Flask(__name__)

# ใส่ Channel Access Token และ Channel Secret ของคุณที่ได้จาก Line Developer Console
line_bot_api = LineBotApi('QN01ycDGxaiS1HGsfVecKp+K9OEWp55wV+Vb5t37JSPh2VouGorNBZhR+lpCucZtTXiUViFJCnjsH9rotOU3E+a5rP+W8Dsd45WiPpXSvT3VPWh7Q0exotCCp/qua9byp7eg3AyNl4NteMYU6WFPtgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('b79ea5129d92d6b867458805cefe29d0')

# สร้าง URL เพื่อดึงข้อมูล JSON
json_url = 'https://api.chnwt.dev/thai-oil-api/latest'

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == 'ดึงข้อมูล':
        # ดึงข้อมูล JSON จาก URL
        response = requests.get(json_url)
        data = response.json()

        # แสดงข้อมูลใน Line
        messages = [TextSendMessage(text=json.dumps(data, indent=2))]
        line_bot_api.reply_message(event.reply_token, messages)

if __name__ == "__main__":
    app.run(port=5000)