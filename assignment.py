from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https://www.amazon.com")
searchField = browser.find_element_by_class_name('nav-input')
browser.find_element_by_xpath()
browser.find_element_by_class_name()

searchField.send_keys("iphone x")
searchField.submit()
