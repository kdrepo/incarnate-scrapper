# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


url = 'https://incarnateword.in/cwsa/34/the-birth-and-childhood-of-the-flame'
wait_time = 4
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(url)
time.sleep(wait_time)
myfile = open("cwsa_34.txt", 'a+', encoding='utf-8')
    
def scrapper():
    heading = driver.find_element(By.TAG_NAME, "h1").get_attribute("outerHTML")
    myfile.write(heading)
    print(heading)
    myfile.write('\n')
    peragraphs = driver.find_elements(By.CLASS_NAME, "text-bg")
    for e in peragraphs:
        pera_html = e.get_attribute("outerHTML")
        myfile.write(pera_html)
        myfile.write('\n')
    myfile.write('\n')
    next = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[3]/div/span[3]/a")
    next.click()
    time.sleep(2)

for x in range(500):
    scrapper()
    print(x)
    
