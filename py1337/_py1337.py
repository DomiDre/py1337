from selenium import webdriver
import time, datetime


def run():
  browser = webdriver.Firefox()
  browser.get('https://web.whatsapp.com/')

  input("Scanned QR Code?")
  target_name = input("Enter target name/group: ")

  user = browser.find_element_by_xpath(f'//span[@title = "{target_name}"]')
  user.click()

  while(True):
    current_time = datetime.datetime.now()
    print(f'It is {current_time.hour}:{current_time.minute}')
    if current_time.hour == 13 and current_time.minute == 37:
      user = browser.find_element_by_xpath(f'//span[@title = "{target_name}"]')
      user.click()
      msg_box = browser.find_element_by_xpath('//div[contains(concat(" ", normalize-space(@class), " "), " selectable-text ")]')
      msg_box.send_keys(f'{current_time.hour}{current_time.minute}')
      browser.find_element_by_class_name('compose-btn-send').click()
    time.sleep(60)
