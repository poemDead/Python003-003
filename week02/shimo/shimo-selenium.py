from selenium import webdriver
import time

try:
    brower = webdriver.Chrome()

    brower.get('https://shimo.im/')
    time.sleep(2)

    login_button = brower.find_element_by_xpath("//div[@class='entries']/a[2]/button")
    login_button.click()

    brower.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div/input').send_keys('mofemo4494@cyberper.net')
    brower.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/input').send_keys('test123geek')
    time.sleep(1)
    brower.find_element_by_xpath("//button[@class='sm-button submit sc-1n784rm-0 bcuuIb']").click()
    time.sleep(60)

    cookies = brower.get_cookies()
    title = brower.title
    print(cookies)
    print(title)

    time.sleep(3)
except Exception as e:
    print(e)
finally:
    brower.close()