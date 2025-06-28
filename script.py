from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()
service = Service(r"C:\Users\CKIRUser\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe")
drivers = [webdriver.Chrome(service=service, options=options),webdriver.Chrome(service=service, options=options),webdriver.Chrome(service=service, options=options)]

urls = ["https://www.youtube.com/watch?v=mIYzp5rcTvU","https://www.github.com"]
i = 0
for url in urls : # URL 띄우기
    i+=1
    drivers[i].set_window_size(100,100)  # 창 크기 조절
    drivers[i].set_window_position(0, i * 100)
    drivers[i].get(url)

i = 0
input("press any key to end")
