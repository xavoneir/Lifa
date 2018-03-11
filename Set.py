from selenium import webdriver

driver = webdriver.Firefox(
    executable_path=r'PATH\\TO\\geckodriver.exe')

page = 'https://quizlet.com/'

driver.get(page)

try:
    driver.find_element_by_class_name('SetPage-seeMore').click()
except:
    pass

a = (driver.find_element_by_class_name('SetPage-termsList').text.split('\n'))
a = [x.encode('utf-8') for x in a]
print(a)

num = 0
num2 = 1

while True:

    if len(a) >= num2:
        with open('quizlet.txt', 'a') as f:
            f.write(str(a[num]) + '\n' + str(a[num2]) + '\n')

        num += 2
        num2 += 2

    else:
        driver.close()
        break
