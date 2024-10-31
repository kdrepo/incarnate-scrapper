# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


url = 'https://incarnateword.in/cwsa/27/three-elements-of-poetic-creation'
wait_time = 4
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(url)
time.sleep(wait_time)
myfile = open("text_27.txt", 'a+', encoding='utf-8')

    
def scrapper():    
    heading = driver.find_element(By.TAG_NAME, "h1").get_attribute("outerHTML")
    myfile.write(heading)
    myfile.write('\n')
    peragraphs = driver.find_elements(By.CLASS_NAME, "para")
    for e in peragraphs:
        pera_html = e.get_attribute("outerHTML")
        myfile.write(pera_html)
        myfile.write('\n')
    myfile.write('\n')
    next = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/div[3]/div/span[3]/a")
    next.click()    
    time.sleep(5)

for x in range(100):
    scrapper()
