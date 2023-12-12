import json

def get_kakao_api_key():
  with open('./token.json', 'r') as f:
    return json.load(f)['access_token']