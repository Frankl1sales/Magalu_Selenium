# webdriver_setup.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def setup_driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    return driver
