import requests
from config import get_kakao_api_key

def get_friends_list():
    api_url = "https://kapi.kakao.com/v1/api/talk/friends"
    kakao_api_key = get_kakao_api_key()

    headers = {
        "Authorization": f"Bearer {kakao_api_key}"
    }

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        print(response.text)
    else:
        print(f"카카오톡 api 실패. 응답 코드: {response.status_code}, 응답 내용: {response.text}")

get_friends_list()
	