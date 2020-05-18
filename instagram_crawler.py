from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import re
import time
import os

#insert your instagram ID, password
ID = ''
PASSWORD = '!'

TAG = 'jeju'
SCROLL_NUMBER = 100
POST_LINK = '#react-root > section > main > article > div:nth-child(3) > div > div > div > a'
USER_NAME = '#react-root > section > main > div > div > article > header > div.o-MQd.z8cbW > div.PQo_0.RqtMr > div.e1e1d > a'
CONTENT = '#react-root > section > main > div > div.ltEKP > article > div.eo2As > div.EtaWk > ul > div > li > div > div > div.C4VMK > span'

#insert chromedriver's path in your directory
d = webdriver.Chrome(os.path.abspath("chromedriver"))

d.get('https://www.instagram.com/explore/tags/'+TAG+'/')
d.implicitly_wait(3)

#login
d.find_element_by_css_selector("#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg > div > span > a:nth-child(1) > button").click()
d.find_elements_by_name("username")[0].send_keys(ID)
d.find_elements_by_name("password")[0].send_keys(PASSWORD)
d.find_element_by_css_selector("#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button").click()
d.implicitly_wait(2)

#get links of post with TAG
scr = SCROLL_NUMBER
links = []
while scr:
	if scr % 4 == 0:
		html = d.page_source
		soup = BeautifulSoup(html, 'html.parser')
		links += soup.select(POST_LINK)
	d.execute_script("window.scrollTo(0, document.body.scrollHeight)")		
	time.sleep(3)
	scr -= 1

#output: <TAG>.csv file
#format: username | content | location
i=0
d.implicitly_wait(1)
tb = pd.DataFrame(columns=['username','content'])
for link in links:
	username = ''
	content = ''

	d.get('https://www.instagram.com'+link.get('href'))

	try:
		username = d.find_element_by_css_selector(USER_NAME).get_attribute("text")
		innerhtml = d.find_element_by_css_selector(CONTENT).get_attribute("innerHTML")
		content = re.sub(re.compile('<.*?>'),'',innerhtml)
	except NoSuchElementException:
		pass
		
	tb.loc[i] = [username,content]
	i+=1
		
tb.to_csv(TAG+".csv")