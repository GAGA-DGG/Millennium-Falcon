from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_experimental_option('androidPackage', 'com.android.chrome')
driver = webdriver.Chrome('./chromedriver', options=options)
driver.get('https://google.com')
driver.quit()
