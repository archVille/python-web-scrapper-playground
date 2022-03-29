from selenium import webdriver 

url = 'https://www.youtube.com/channel/UCLocmFIOWIZqpoGIaWr8m7g'
browser = webdriver.Chrome()
browser.get(url)

browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div/div/button/span').click() #agree with terms

browser.find_element_by_xpath('//*[@id="tabsContent"]/tp-yt-paper-tab[2]/div').click()


