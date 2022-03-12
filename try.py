from selenium import webdriver

instance=webdriver.Chrome('chromedriver.exe')
instance.get('https://chartink.com/login')