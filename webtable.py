from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# Set Chrome options
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

# Initialize Chrome browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Load the website
driver.get("https://testautomationpractice.blogspot.com/")

# ----------------------------------------------------
# Capture number of rows and columns in the table
# ----------------------------------------------------
rows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr"))
columns = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr[1]/th"))

print(f"Total number of rows: {rows}")
print(f"Total number of columns: {columns}")

# ----------------------------------------------------
# Capture specific cell data (e.g., 5th row, 1st column)
# ----------------------------------------------------
cell_data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[5]/td[1]").text
print(f"\nData at row 5, column 1: {cell_data}")

# ----------------------------------------------------
# Print all data from the table (except header)
# ----------------------------------------------------
print("\nAll table data:")
for r in range(2, rows + 1):
    for c in range(1, columns + 1):
        cell = driver.find_element(By.XPATH, f"//table[@name='BookTable']/tbody/tr[{r}]/td[{c}]").text
        print(cell, end='  ')
    print()

# ----------------------------------------------------
# Conditional data extraction: Books by author "Mukesh"
# ----------------------------------------------------
print("\nBooks by author 'Mukesh':")
for r in range(2, rows + 1):
    author = driver.find_element(By.XPATH, f"//table[@name='BookTable']/tbody/tr[{r}]/td[2]").text
    if author == "Mukesh":
        book_name = driver.find_element(By.XPATH, f"//table[@name='BookTable']/tbody/tr[{r}]/td[1]").text
        price = driver.find_element(By.XPATH, f"//table[@name='BookTable']/tbody/tr[{r}]/td[4]").text
        print(f"{book_name}     {author}     {price}")

# Optional: Wait and then close the browser
time.sleep(3)
driver.quit()
