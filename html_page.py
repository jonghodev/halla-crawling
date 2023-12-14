import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(chrome_options)
driver.set_page_load_timeout(10)

url = "https://visithalla.jeju.go.kr/reservation/status.do?language=ko_KR"

def fetch_html(is_next_page, is_next_dropbox):
  if not is_next_page and not is_next_dropbox:
    response = requests.get(url)
    html = response.text
    return html

  crawling_success = False
  for i in range(5):
    print(f'try  count: {i + 1}')
    try:
      driver.get(url)
      if is_next_dropbox:
        select = Select(driver.find_element(By.XPATH,'//*[@id="courseSeq"]'))
        select.select_by_index(1)
      if is_next_page:
        driver.find_element(By.XPATH,'//*[@id="sub_contents"]/div/div/div/div[1]/a[2]').click()
      crawling_success = True
    except Exception as ex:
      print(f'try  count: {i + 1} =>\nexception: {ex}')
    if crawling_success == True:
      break
    time.sleep(5)
  if crawling_success == False:
    raise Exception('Retry failed')
  
  return driver.page_source