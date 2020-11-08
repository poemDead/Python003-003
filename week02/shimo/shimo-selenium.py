from selenium import webdriver
import time

try:
    brower = webdriver.Chrome()

    brower.get('https://shimo.im/login?from=home')
    time.sleep(2)

    brower.find_element_by_name('mobileOrEmail').send_keys('mofemo4494@cyberper.net')
    brower.find_element_by_name('password').send_keys('test123geek')
    time.sleep(1)
    brower.find_element_by_xpath("//button[@class='sm-button submit sc-1n784rm-0 bcuuIb']").click()
    time.sleep(10)

    cookies = brower.get_cookies()
    title = brower.title
    print(cookies)
    print(title)

    time.sleep(3)
except Exception as e:
    print(e)
finally:
    brower.close()