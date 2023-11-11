import time
begin = time.time()

print(begin)

# if not (begin <= time.time() <= begin + 60):
#     break
    
# import json
# from flask import Flask, request, jsonify
# import requests
# app = Flask(__name__)


# @app.route("/webhook", methods=["POST"])
# def webhook():
#     data = request.get_json()
#     # ดึงข้อมูล JSON จาก data และทำตามที่คุณต้องการ
#     return "OK"

# def send_message(channel_access_token, user_id, text):
#     url = "https://api.line.me/v2/bot/message/push"
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {channel_access_token}",
#     }
#     data = {"to": user_id, "messages": [{"type": "text", "text": text}]}
#     response = requests.post(url, headers=headers, json=data)

    

# url = "https://api.chnwt.dev/thai-oil-api/latest"
# res = requests.get(url)

# data = res.json()
# ptt = data["response"]["stations"]["ptt"]
# date = data["response"]["date"]
# gasoline_95 = (
#     ptt["gasoline_95"]["name"] + " ราคา: " + ptt["gasoline_95"]["price"] + " บาท"
# )
# gasohol_95 = (
#     ptt["gasohol_95"]["name"] + " ราคา: " + ptt["gasohol_95"]["price"] + " บาท"
# )
# gasohol_91 = (
#     ptt["gasohol_91"]["name"] + " ราคา: " + ptt["gasohol_91"]["price"] + " บาท"
# )
# gasohol_e20 = (
#     ptt["gasohol_e20"]["name"] + " ราคา: " + ptt["gasohol_e20"]["price"] + " บาท"
# )
# gasohol_e85 = (
#     ptt["gasohol_e85"]["name"] + " ราคา: " + ptt["gasohol_e85"]["price"] + " บาท"
# )
# diesel = ptt["diesel"]["name"] + " ราคา: " + ptt["diesel"]["price"] + " บาท"
# diesel_b7 = (
#     ptt["diesel_b7"]["name"] + " ราคา: " + ptt["diesel_b7"]["price"] + " บาท"
# )
# diesel_b20 = (
#     ptt["diesel_b20"]["name"] + " ราคา: " + ptt["diesel_b20"]["price"] + " บาท"
# )
# premium_diesel = (
#     ptt["premium_diesel"]["name"]
#     + " ราคา: "
#     + ptt["premium_diesel"]["price"]
#     + " บาท"
# )
# premium_gasohol_95 = (
#     ptt["premium_gasohol_95"]["name"]
#     + " ราคา: "
#     + ptt["premium_gasohol_95"]["price"]
#     + " บาท"
# )
# superpower_gasohol_95 = (
#     ptt["superpower_gasohol_95"]["name"]
#     + " ราคา: "
#     + ptt["superpower_gasohol_95"]["price"]
#     + " บาท"
# )
# json_data = (
#     gasoline_95,
#     gasohol_95,
#     gasohol_91,
#     gasohol_e20,
#     gasohol_e85,
#     diesel,
#     diesel_b7,
#     diesel_b20,
#     premium_diesel,
#     premium_gasohol_95,
#     superpower_gasohol_95,
# )
# # ทำการจัดรูปแบบข้อมูล JSON ตามที่คุณต้องการ
# # ยังสามารถทำการวนลูปข้อมูลและส่งข้อมูลกลับไปยัง LINE
# response1 = f"ราคาน้ำมัน Update : {date}\n"
# # for key, value in json_data.items():
# #     response += f"{key}: {value}\n"
# for i in json_data:
#     response1 += f"{i}\n"
# # ใช้ฟังก์ชัน send_message เพื่อส่งข้อความไปยัง Line
# send_message(
#     "QN01ycDGxaiS1HGsfVecKp+K9OEWp55wV+Vb5t37JSPh2VouGorNBZhR+lpCucZtTXiUViFJCnjsH9rotOU3E+a5rP+W8Dsd45WiPpXSvT3VPWh7Q0exotCCp/qua9byp7eg3AyNl4NteMYU6WFPtgdB04t89/1O/w1cDnyilFU=",
#     "U5bc46a7d0b9480beefd4d8137b5c332c",
#     response1,
# )

# if __name__ == "__main__":
#     app.run()
