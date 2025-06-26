from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
# Options
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://practice.expandtesting.com/dynamic-table")

noofrows = len(driver.find_elements(By.XPATH, "//table[@class='table table-striped']/tbody/tr"))
print(noofrows)

for r in range(1, noofrows + 1):
    name = driver.find_element(By.XPATH, "//table[@class='table table-striped']/tbody/tr[" + str(r) + "]/td[1]").text
    if name == "Chrome":
        cpuvalue = driver.find_element(By.XPATH, "//td[normalize-space()='Chrome']/following-sibling::*[contains(text(),'%')]").text
        actualvalue = driver.find_element(By.XPATH,"//p[@id='chrome-cpu']").text
        print(cpuvalue)
        print(actualvalue)
        if cpuvalue in actualvalue:
          print("it is contained")
        else:
           print("it is not contained")



time.sleep(5)