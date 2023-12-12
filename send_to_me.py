import requests
from config import get_kakao_api_key
import json

kakao_api_key = "JSt2VMLy1Y3AS_hSj5KZyIUJsOPgysHys18KPXLqAAABjFzloxhAPV-WDrAHcw"

def send_kakao_message_to_me(text):
    api_url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
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
        "template_object": json.dumps(template_object)
    }

    # 카카오톡 메시지 전송
    response = requests.post(api_url, headers=headers, data=data)

    # 응답 확인
    if response.status_code == 200:
        print("카카오톡 메시지 전송 성공")
    else:
        print(f"카카오톡 메시지 전송 실패. 응답 코드: {response.status_code}, 응답 내용: {response.text}")
