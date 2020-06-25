import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "http://suninjuly.github.io/explicit_wait2.html"
#browser = webdriver.Chrome('C:\WORK\AllDrivers\chromedriver.exe')
browser = webdriver.Chrome('')
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)
wait = WebDriverWait(browser, 13) #explicitwaiter - явные

try:

    browser.get(link)
    price = browser.find_element_by_id("price")
    wait.until(
        EC.text_to_be_present_in_element ((By.ID, "price"), "$100")
    )

    browser.find_element_by_id("book").click()

    input_val = browser.find_element_by_id("input_value")

    xxx = browser.find_element_by_id("input_value").text
    print(xxx)
    yyy = str(math.log(abs(12 * math.sin(int(xxx)))))

    # Напишем текст ответа в найденное поле
    browser.find_element_by_id("answer").send_keys(yyy)
    browser.find_element_by_id("solve").click()


finally:
    time.sleep(10)
    browser.quit()
