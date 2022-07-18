#Small test using Selenium to open a page automatically

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website = "https://www.visualcapitalist.com/"
path = '/Users/dougl/Downloads/chromedriver_win32/chromedriver.exe'

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)
