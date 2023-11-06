from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    # ดึงข้อมูล JSON จาก data และทำตามที่คุณต้องการ
    return 'OK'
import requests

def send_message(channel_access_token, user_id, text):
    url = 'https://api.line.me/v2/bot/message/push'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {channel_access_token}'
    }
    data = {
        'to': user_id,
        'messages': [{'type': 'text', 'text': text}]
    }
    response = requests.post(url, headers=headers, json=data)

# ใช้ฟังก์ชัน send_message เพื่อส่งข้อความไปยัง Line
send_message('QN01ycDGxaiS1HGsfVecKp+K9OEWp55wV+Vb5t37JSPh2VouGorNBZhR+lpCucZtTXiUViFJCnjsH9rotOU3E+a5rP+W8Dsd45WiPpXSvT3VPWh7Q0exotCCp/qua9byp7eg3AyNl4NteMYU6WFPtgdB04t89/1O/w1cDnyilFU=', 'U5bc46a7d0b9480beefd4d8137b5c332c', 'Hello, LINE!')

if __name__ == '__main__':
    app.run()
