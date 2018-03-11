from selenium import webdriver
import time

joincode = "828520"                   #Join code for Quizlet.live
name = "Account Name"                       #Name for Quizlet.live
initial = "_"                    #In case of duplicates, Quizlet may ask for an initial

with open('quizlet.txt', 'r') as file:
    page = file.read().split('\n')

driver = webdriver.Firefox(executable_path=r'C:\\Users\\Chan\\Desktop\\Python\\Gen\\SelDrivers\\geckodriver.exe')

driver.get('https://quizlet.com/live')
driver.find_element_by_class_name('UIInput-input').send_keys(joincode)
driver.find_element_by_class_name('UIButton-wrapper').click()
time.sleep(0.5)
driver.find_element_by_class_name('UIInput-input').send_keys(name)
driver.find_element_by_class_name('UIButton-wrapper').click()
try:
    time.sleep(0.5)
    driver.find_element_by_class_name('UIInput').send_keys('_')
    driver.find_element_by_class_name('UIButton-wrapper').click()
except:
    pass



while(True):
    try:
        question = driver.find_element_by_class_name('StudentPrompt-inner').text.encode('utf-8')
        print(question)
        possible_answer = driver.find_element_by_class_name('StudentTermGroup-terms').text.encode('utf-8')
        print(answer)
    except:
        pass
