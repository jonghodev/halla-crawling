import time
import sys
import schedule
from bs4 import BeautifulSoup

from send_to_me import send_kakao_message_to_me
from send_to_friend import send_kakao_message_to_friend
from refresh_token import refresh
from html_page import fetch_html

sys.stdout.flush()

def job(target, is_next_page, is_next_dropbox):
  try:
    html = fetch_html(is_next_page, is_next_dropbox)
    soup = BeautifulSoup(html, 'html.parser')

    available_dates = soup.select(target)
    for date in available_dates:
      arr = date.text.strip().split()
      reservation_date = int(arr[0])
      reservation_date_text = f'12월 {reservation_date}일' if reservation_date > 10 else f'1월 {reservation_date}일'
      path_text = '성판악' if is_next_dropbox else '관음사'
      remain_count = int(arr[2])

      if remain_count > 0:
        text = f'{path_text} {reservation_date_text} 일자에 찾았습니다.\n남은 개수: {remain_count}'
        send_kakao_message_to_me(text)
        send_kakao_message_to_friend(text)
        print(text)
      else:
        print(f'{path_text} {reservation_date_text} 일자에 찾지 못했습니다.')
  except Exception as e:
    print(f'에러 발생: {e}')
  
schedule.every(10).seconds.do(lambda: job('#TD_20231231', False, False)) # 12.31 성판악
schedule.every(10).seconds.do(lambda: job('#TD_20231231', False, True)) # 12.31 관음사
schedule.every(10).seconds.do(lambda: job('#TD_20240101', True, False)) # 1.1 성판악
schedule.every(10).seconds.do(lambda: job('#TD_20240101', True, True)) # 1.1 관음사

schedule.every(60).minutes.do(refresh) # Token Refresh

while True:
    schedule.run_pending()
    time.sleep(1)