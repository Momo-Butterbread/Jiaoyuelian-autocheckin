import json
import sys
from os import environ
import requests

def send_notification(message):
    # 读取企业微信机器人的 webhook 地址
    webhook_url = environ.get('WECOM_WEBHOOK')
    if not webhook_url:
        return 'WeCom: No webhook configured, cannot send notification.'

    # 企业微信机器人消息格式：text
    data = {
        "msgtype": "text",
        "text": {
            "content": "皎月连签到：" + message
        }
    }

    headers = {'Content-Type': 'application/json'}
    rsp = requests.post(webhook_url, data=json.dumps(data), headers=headers)
    return rsp.text

if __name__ == '__main__':
    if len(sys.argv) > 1:
        checkin_message = sys.argv[1]
        print(send_notification(checkin_message))
    else:
        print("Usage: python push_notification.py <checkin_message>")
        sys.exit(1)
