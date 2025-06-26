from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Options
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://cosmocode.io/automation-practice-webtable/#google_vignette")

noofrows = len(driver.find_elements(By.XPATH, "//table[@id='countries']/tbody/tr"))
noofcolumns = len(driver.find_elements(By.XPATH, "//table[@id='countries']/tbody/tr[1]/td"))
print(f"Rows: {noofrows}, Columns: {noofcolumns}")

for r in range(1, noofrows + 1):
    for c in range(1, noofcolumns + 1):
        cell = driver.find_element(By.XPATH, f"//table[@id='countries']/tbody/tr[{r}]/td[{c}]").text
        print(cell, end=" | ")
    print()
for r in range(1, noofrows + 1):
    # XPath for 2nd column cell in row r
    cell_xpath = f"//table[@id='countries']/tbody/tr[{r}]/td[2]"
    cell = driver.find_element(By.XPATH, cell_xpath)
    print(cell.text)


driver.quit()
