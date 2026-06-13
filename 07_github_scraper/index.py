import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

repo_name = "https://github.com/BoKu237723"

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

# repo = input("Enter the repo you would like to target: ")

driver.get(repo_name)
time.sleep(2)

res = driver.find_elements(By.CLASS_NAME, "repo")
time.sleep(2)

links = []
flink = []

# def loop(next_page):
    # print(f"Scanning: {next_page}")
    # driver.get(next_page)
    # time.sleep(2)
    # res2 = driver.find_elements(By.CLASS_NAME, "Link--primary")
    # for i in res2:
        # print(i.text)

def going_for_raw(individual_files):
    raw = driver.find_element(By.CLASS_NAME, "prc-Button-Label-FWkx3")
    raw.click()
    html = driver.page_source
    html = f"{html}"
    key = "pickle"
    if key in html:
        print(f"Found {key} in {individual_files}")

def loop(next_page):
    print(f"\nScanning: {next_page}")
    driver.get(next_page)
    time.sleep(2)
    res2 = driver.find_elements(By.CLASS_NAME, "Link--primary")

    for i in res2:
        if "py" in i.text: # if there is a python file in repo....
            second_page = f"{next_page}/blob/main/{i.text}"
            print(f".py file found in the repo: {next_page}")
            print(second_page)
            going_for_raw(second_page)
            # time.sleep(1)
        else:
            pass

for i in res:
    links.append(i.text)

print(links)
for l in links:
    next_page = f"{repo_name}/{l}"
    flink.append(next_page)
    loop(next_page)

driver.quit()


