from selenium import webdriver
import time

joincode = "864712"                   #Join code for Quizlet.live
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

while True:
    num = 1
    print('Ok!')
    while True:
        try:
            print('num: ' + str(num))
            possible_answer = str(driver.find_element_by_xpath('/html/body/div[2]/main/div/div/div[1]/div/div/span/div/div[' + str(num) + ']/div/div[2]').text.encode('utf-8'))    #All possible answers MAIN
            print('still at: ' + possible_answer)
            if possible_answer != 'b\'\'':                                     #/html/body/div[2]/main/div/div/div[1]/div/div/span/div/div[2]/div/div[2] error right
                print('possible_answer init: ' + possible_answer)         #/html/body/div[2]/main/div/div/div[1]/div/div/span/div/div[1]/div/div[2]
                break

            if num >= 5:
                num = 1
            else:
                num += 1
        except:
            pass

    while True:
        question = driver.find_element_by_class_name('StudentPrompt-inner').text.encode('utf-8')  # Question
        print('question: ' + str(question))
        real_possible_answer = driver.find_element_by_class_name('StudentTermGroup-terms').text.encode('utf-8')  #All possible answers CHECK
        if not (all(x in possible_answer for x in real_possible_answer.split())):
            possible_answer = driver.find_element_by_xpath('/html/body/div[2]/main/div/div/div[1]/div/div/span/div/div[' + str(num) + ']/div/div[2]').text.encode('utf-8')  # My Answers
