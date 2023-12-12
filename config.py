import json

def get_kakao_api_key():
  with open('./token.json', 'r') as f:
    return json.load(f)['access_token']
  
def get_kakao_refresh_token():
  with open('./token.json', 'r') as f:
    return json.load(f)['refresh_token']