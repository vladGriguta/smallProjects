
import requests
import re
from bs4 import BeautifulSoup


URL = ('https://www.amazon.co.uk/Samsung-Galaxy-Dual-SIM-Android-Smartphone-Prism-Black/'
       'dp/B07NWR7QYQ/ref=sr_1_3?dchild=1&keywords=galaxy+s10&qid=1592944411&s=electronics&sr=1-3')


headers = {'User-Agent': ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
           '(KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36')}

def check_page():
	page = requests.get(URL, headers=headers)

	soup1 = BeautifulSoup(page.content, "html.parser")
	# need to use a second soup because of the javascript generator of html
	soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

	title = soup2.find(id= "productTitle").get_text()

	price = soup2.find(id='priceblock_ourprice').get_text()

	converted_price = price[1:].replace(',','').split('.')[0]

	print(title)
	print(converted_price)