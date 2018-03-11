from selenium import webdriver
import time

joincode = "724302"                   #Join code for Quizlet.live
name = "Account Name"                       #Name for Quizlet.live
initial = "_"                    #In case of duplicates, Quizlet may ask for an initial

with open('quizlet.txt', 'r') as file:
    page = file.read().split('\n')
print(page)

driver = webdriver.Firefox(executable_path=r'PATH\\TO\\geckodriver.exe')

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
print('Ready!')


# POSSIBLE ANSWERS WIP, QUESTION CURRENTLY WORKING
while True:

    while True:
        try:
            possible_answer = driver.find_element_by_class_name('StudentTermGroup-terms').text.encode('utf-8')  #All possible answers MAIN
            print('possible_answer: ' + possible_answer)
            if possible_answer != '':
                break
        except:
            pass

    while True:
        question = driver.find_element_by_class_name('StudentPrompt-inner').text.encode('utf-8')  # Question
        print('question: ' + question)
        real_possible_answer = driver.find_element_by_class_name('StudentTermGroup-terms').text.encode('utf-8')  #All possible answers CHECK

        if not (all(x in possible_answer for x in real_possible_answer.split())):
            possible_answer = (driver.find_element_by_xpath('/html/body/div[2]/main/div/div/div[1]/div/div/span/div/div[' + str(num) + ']/div/div[2]').text)  # My Answers
