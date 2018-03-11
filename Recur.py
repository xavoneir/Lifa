from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

joincode = '969060'

words = (
'Hey, Vsauce, Michael here! Down here. But which way is down? And how much does down weigh? Well, down weighs '
'about 1/100 of a g/cm3. It is light, and airy, which makes it a great source of insulation and buoyancy for '
'waterbirds. But if you let go of down, it falls down. So that\'s which way down is, it\'s the direction that '
'gravity is pulling everything. Now for someone on the other side of the Earth, my down is their up, but where '
'are falling things going? Why do things fall? Are they being pushed or pulled? Or, is it because of TIME TRAVEL!').split()

driver = webdriver.Firefox(
    executable_path=r'PATH\\TO\\geckodriver.exe')

driver.get('https://quizlet.com/live')
a = 0
x = 0
while a == 0:
    WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_class_name('UIInput-input'))
    if driver.find_element_by_class_name('UIDiv').text == 'Your teacher will give you a join code.':
        driver.find_element_by_class_name('UIInput-input').send_keys(joincode)
        driver.find_element_by_class_name('UIButton-wrapper').click()
        time.sleep(0.5)
        if 'CODE' in driver.find_element_by_class_name('UIInput-label').text:
            a = 1
        driver.find_element_by_class_name('UIInput-input').send_keys(words[x])
        driver.find_element_by_class_name('UIButton-wrapper').click()
        try:
            driver.find_element_by_class_name('UIDiv')
            if driver.find_element_by_class_name('UIDiv').text == 'What\'s your last initial?':
                driver.find_element_by_class_name('UIInput-input').send_keys('☯')
                driver.find_element_by_class_name('UIButton-wrapper').click()
                driver.delete_all_cookies()
                driver.refresh()
                try:
                    driver.switch_to.alert.accept()
                except:
                    driver.get('https://quizlet.com/live')
                x += 1
            else:
                driver.delete_all_cookies()
                driver.refresh()
                try:
                    driver.switch_to.alert.accept()
                except:
                    driver.get('https://quizlet.com/live')
                x += 1
        except:
            driver.delete_all_cookies()
            driver.refresh()
            try:
                driver.switch_to.alert.accept()
            except:
                driver.get('https://quizlet.com/live')
            x += 1
    if len(words) == x:
        a = 1

driver.close()
