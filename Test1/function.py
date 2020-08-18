from bs4 import BeautifulSoup
import urllib.request
from testFun import post


def xulyUser(user):
    if('/user/show/' in user):
        user = user.replace('/user/show/', '')
        if '-' in user:
            user = user[:user.index('-')]
    return int(user)

def xulyBook(data):
    page = urllib.request.urlopen(data['link'])
    soup = BeautifulSoup(page, 'html.parser')
    rate = soup.find('div', id='topcol').find('div', id='metacol').find('div', id='bookMeta').find('span',
                                                                                                   itemprop="ratingValue")
    data['rate'] = float((rate.text))#.replace('\n', '').replace(' ', ''))
    book = soup.find('div', id="description", class_="readable stacked").find('span', style="")
    data['description'] = book.text
    data['review'] = []
    reviews = soup.find('div', id="bookReviews").findAll('div', class_="friendReviews elementListBrown")
    for review in reviews:
        data_review = {}
        content = review.find('div', class_="reviewText stacked").find('span', class_="readable").find('span', style=None)
        name = review.find('div', class_="reviewHeader uitext stacked").find('span', itemprop="author").find('a')
        date_post = review.find('div', class_="reviewHeader uitext stacked").find('a',
                                                                                 class_="reviewDate createdAt right")
        rate = review.find('div', class_="reviewHeader uitext stacked").findAll('span',
                                                                            class_="staticStar p10")
        # comment = review.find('div', class_="reviewFooter uitext buttons").findAll('div')[1]
        data_review['id_user'] = xulyUser(name.get('href'))
        data_review['name_user'] = name.get('name')
        data_review['rate'] = len(rate)
        data_review['review_content'] = content.text
        # data_review['list_comment'] = comment
        data_review['date_post'] = date_post.text
        data['review'].append(data_review)
    return data


def inputToDB(arrData):
    for data in arrData:
        post(data)


