from selenium import webdriver
browser=webdriver.Edge("C:/Users/MrMaak/Downloads/msedgedriver")
userin=input("Search for:")
browser.get("https://www.google.com/search?q="+userin)
results = browser.find_elements_by_xpath('//div[@class="r"]/a/h3')
results[0].click()