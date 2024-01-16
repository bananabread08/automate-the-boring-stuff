from selenium import webdriver

# opens firefox
browser = webdriver.Firefox()

# go to URL while in firefox
browser.get('URL_HERE')

# get the html element
elem = browser.find_element_by_css_selector('SELECTOR')
elem.click()

# add keys. example in a search bar
elem.send_keys('KEYS')
elem.submit()

# browser actions
browser.back()
browser.forward()
browser.refresh()
browser.quit()

# get string inside the element
elem.text

