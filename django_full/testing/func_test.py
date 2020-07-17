from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://127.0.0.1:8000')

assert browser.page_source.find('install')