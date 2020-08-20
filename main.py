
from time import sleep
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def clickGoldenCookie():
    try:
        driver.find_element_by_class_name('shimmer').click()
        print('[o] clicked Golden cookie')
    except:
        pass


PATH = 'C:/Program Files (x86)/WebDriver/msedgedriver.exe'

driver = webdriver.Edge(PATH)
print(driver.title)

driver.get("https://orteil.dashnet.org/cookieclicker/")
print(driver.title)

try:
    main = WebDriverWait(driver,20).until(
        # EC.presence_of_all_elements_located((By.ID, 'prefsButton'))
        EC.presence_of_all_elements_located((By.ID, 'bigCookie'))
    )
    sleep(4)

    print('[o] hey u found it')
    # print(driver.page_source)

except:
    print('[X] err')
    sleep(5)
    driver.quit()

driver.find_element_by_id('prefsButton').click()
saving_path = 'C:/Users/tim10n/Downloads/CookieBakery.txt'
driver.find_element_by_id('FileLoadInput').send_keys(saving_path)

#get all the items ava to buy
while True:
    items=driver.find_elements_by_class_name('product.unlocked.enabled')

    clickGoldenCookie()
    for i in reversed(items[8:]):
        i.click()
        print('clicked : ' + i.find_element_by_class_name('title').text +
              '['+ i.find_element_by_class_name('title.owned').text +']')
    # sleep(10)
    for i in range(70):
        driver.find_element(By.ID, 'bigCookie').click()
    sleep(3)



# search = driver.find_element_by_name("q")   #this is to find the search tag
# search.send_keys("test", Keys.ARROW_DOWN)  #this is the text wnat to search
# search.send_keys(Keys.RETURN)   #this means enter
#
# try:
#     main = WebDriverWait(driver,10).until(
#         EC.presence_of_all_elements_located((By.ID, "search"))
#     )
#
#     print('[o] hey u found it')
#     # print(driver.page_source)
# except:
#     print('[X] err')
#
# sleep(1)
#
# # results = driver.find_element_by_class_name('g')
# results = driver.find_elements_by_class_name('g')
# # print(results.text)
# print(len(results))
# sleep(5)
# driver.quit()

# driver.find_element()