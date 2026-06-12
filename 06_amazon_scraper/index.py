import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# cdp = "/home/kali/Desktop/Extensions/chromedriver/linux-149.0.7827.102/chromedriver-linux64/"
# driver = webdriver.Chrome(executable_path = cdp)
# these are old codes and won't work anymore

# ====================
# s = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=s)

# driver = webdriver.Chrome()
# driver.get("https://google.com")
# driver.quit()
# ====================


while True:
    def five_seconds():
        time.sleep(5)
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
        
        driver = webdriver.Chrome()
        driver.get("https://www.amazon.com/Tool-Kit-21V-Cordless-Drill/dp/B0D41LXCF2/ref=pd_sbs_d_sccl_1_4/137-3136218-3808428?pd_rd_w=QiZpU&content-id=amzn1.sym.aa738fbd-ad05-4d11-aae2-04b598db6305&pf_rd_p=aa738fbd-ad05-4d11-aae2-04b598db6305&pf_rd_r=EWJ6R0HYMSQNRKDB848M&pd_rd_wg=U6lTR&pd_rd_r=2a4c813c-8cb7-44a7-a16f-6356d522ddd2&pd_rd_i=B0D41LXCF2&psc=1")
        price = driver.find_element(By.CLASS_NAME, "p13n-sc-price")
        print(price.text)
        driver.quit()

    five_seconds()







# 149.0.7827.102























