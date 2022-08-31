import time
from selenium import webdriver
import random

print("https://chromedriver.chromium.org/downloads")
url = input("Enter The URL Below: ")  # 'https://www.neoenbd.com/#/register?inviteCode=871424'
acc_num = int(input("How many account you want to generate : "))

for i in range(acc_num):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    # driver = webdriver.Chrome(executable_path="<path of chrome_driver.exe file>",options=chrome_options)

    driver = webdriver.Chrome(executable_path="C:\\Users\\Himu\\Downloads\\chromedriver_win32\\chromedriver.exe",options=chrome_options)
    time.sleep(1)
    driver.get(url)
    num_list = []

    num_gen = random.randrange(999999, 100000000)
    num_gen = f"1{num_gen}"
    pass_gen = "12345678"

    with open("Account.txt", "a") as file_object:
        file_object.write(f"\n+880{num_gen}")

    if num_gen not in num_list:
        driver.find_element_by_xpath("//*[@id='app']/div[1]/div[3]/div[1]/div[1]/div[3]/div/input").send_keys(num_gen)
        driver.find_element_by_xpath("//*[@id='app']/div[1]/div[3]/div[1]/div[2]/div[2]/div/input").send_keys(pass_gen)
        driver.find_element_by_xpath("//*[@id='app']/div[1]/div[3]/div[1]/div[3]/div[2]/div/input").send_keys(pass_gen)
        create = driver.find_element_by_xpath("//*[@id='app']/div[1]/div[3]/button").click()
        print(num_gen)
        num_list.append(num_gen)
        driver.close()
        time.sleep(3)
