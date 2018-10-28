from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
options.binary_location = '/usr/bin/google-chrome-stable'
options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=options)

missionchan = 'https://e-hentai.org/s/7b1b30f886/409815-1'
count = 1
count_max = 218
img_width = 450
img_height = 600
wait = 1

driver.set_window_size(img_width, img_height)
driver.get(missionchan)
while count <= count_max:
    imgurl = driver.find_element_by_id('img').get_attribute('src')
    driver.get(imgurl)
    if driver.save_screenshot(str(count) + '.png'):
        print(imgurl)
    driver.back()
    driver.find_element_by_id('next').click()
    count += 1
    sleep(wait)
