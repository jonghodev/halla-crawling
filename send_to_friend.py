import requests
from config import get_kakao_api_key
import json

def send_kakao_message_to_friend(text):
    api_url = "https://kapi.kakao.com/v1/api/talk/friends/message/default/send"
    kakao_api_key = get_kakao_api_key()

    headers = {
        "Authorization": f"Bearer {kakao_api_key}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    template_object = {
        "object_type": "text",
        "text": text,
        "link": {
            'web_url': 'https://visithalla.jeju.go.kr/reservation/status.do',
            'mobile_web_url': 'https://visithalla.jeju.go.kr/reservation/status.do'
        },
        'button_title': '예약하러 가기'
    }

    data = {
        "template_object": json.dumps(template_object),
        "receiver_uuids": json.dumps(["d0V9Sn1FdUx1WWteblptVGRTZ0t6SnpDc0t5DA", "d0J6TH9HdkZyXm9ca1lsWGtabEBxQXFIeEByGw"])
    }

    # 카카오톡 메시지 전송
    response = requests.post(api_url, headers=headers, data=data)

    # 응답 확인
    if response.status_code == 200:
        print("카카오톡 메시지 전송 성공")
    else:
        print(f"카카오톡 메시지 전송 실패. 응답 코드: {response.status_code}, 응답 내용: {response.text}")
