import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
url = "https://visithalla.jeju.go.kr/reservation/status.do?language=ko_KR"

def fetch_html(is_next_page, is_next_dropbox):
  if not is_next_page and not is_next_dropbox:
    response = requests.get(url)
    html = response.text
    return html

  driver.get(url)
  if is_next_dropbox:
    select = Select(driver.find_element(By.XPATH,'//*[@id="courseSeq"]'))
    select.select_by_index(1)
  if is_next_page:
    driver.find_element(By.XPATH,'//*[@id="sub_contents"]/div/div/div/div[1]/a[2]').click()
  
  return driver.page_source