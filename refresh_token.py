import requests
import json
from config import get_kakao_refresh_token

def refresh():
    api_url = "https://kauth.kakao.com/oauth/token"
    refresh_token = get_kakao_refresh_token()

    headers = {
        "Authorization": f"Bearer {refresh_token}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        'grant_type': 'refresh_token',
        'client_id': 'a807afb2e53a8b48ea9e3d64ef1610f8',
        'refresh_token': refresh_token
    }

    # 카카오톡 메시지 전송
    response = requests.post(api_url, headers=headers, data=data)

    # 응답 확인
    if response.status_code == 200:
        print(f"리프레시 성공 응답 내용: {response.text}")
        new_access_token = json.loads(response.text)['access_token']
        update_json(new_access_token)
    else:
        print(f"리프레시 실패. 응답 코드: {response.status_code}, 응답 내용: {response.text}")

def update_json(access_token):
  with open("./token.json", "r") as jsonFile:
      data = json.load(jsonFile)

  data["access_token"] = access_token

  with open("./token.json", "w") as jsonFile:
      json.dump(data, jsonFile)
