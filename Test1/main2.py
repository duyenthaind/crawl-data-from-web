from bs4 import BeautifulSoup
import urllib.request
import function
import json


url = 'https://www.goodreads.com/author/list/4634532.Nguy_n_Nh_t_nh?page=1&per_page=30'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

books = soup.find('table', class_="tableList").findAll('tr', itemtype="http://schema.org/Book")

sum = []
for feed in books:
	fee1 = feed.find('a')
	fee2 = feed.find('div', class_="u-anchorTarget")
	fee3 = feed.find('a', class_="authorName")
	# fee4 = feed.find('span', class_="greyText smallText uitext")
	title = fee1.get('title')
	link = fee1.get('href')
	id = int(fee2.get('id'))
	sum.append({'title': title, 'link': 'https://www.goodreads.com'+link, 'id' : id, 'author': fee3.text})

for book in sum:
	book = function.xulyBook(book)

choose = int(input('chon 1 de dua du lieu vao DB, 2 de cho data vao file data.txt: '))
if choose == 1:
	function.inputToDB(sum)
	print("ok")
else:
	with open('data.txt', 'w', encoding='utf8') as outfile:
		json.dump(sum, outfile, ensure_ascii=False)

