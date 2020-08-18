from bs4 import BeautifulSoup
import urllib.request

# def xulyUser(user):
#     user = user.replace('/user/show/', '')
#     user = user[:user.index('-')]
#     return int(user)
#
# url = 'https://www.goodreads.com/book/show/10925109-cho-t-i-xin-m-t-v-i-tu-i-th'
# page = urllib.request.urlopen(url)
# soup = BeautifulSoup(page, 'html.parser')
#
# rate = soup.find('div', id='topcol').find('div', id='metacol').find('div', id='bookMeta').find('span', itemprop="ratingValue")
# rate = rate.text
# print(rate)
# list_comment = soup.find('div', id="bookReviews").findAll('div', class_="friendReviews elementListBrown")
# lis = []
# for comment in list_comment:
#     data_review = {}
    # content = comment.find('div', class_="reviewText stacked").find('span', class_="readable").find('span', style=None)
    # name = comment.find('div', class_="reviewHeader uitext stacked").find('span', itemprop="author").find('a')
    # date_post = comment.find('div', class_="reviewHeader uitext stacked").find('a', class_="reviewDate createdAt right")
    # rate = comment.find('div', class_="reviewHeader uitext stacked").findAll('span', class_="staticStar p10")
    # comments = comment.find('div', class_="reviewFooter uitext buttons").findAll('div')
    # comments = comments.findAll('div')
    # data_review['id_user'] = xulyUser(name.get('href'))
    # data_review['name_user'] = name.get('name')
    # data_review['rate'] = len(rate)
    # data_review['review_content'] = content.text
    # data_review['date_post'] = date_post.text
    # print(comments)
    # break
    # data_review['list_comment'] = []
    # for com in comments:
    #     # commen = com.find('div')
    #     # co = commen
    #     data_review['list_comment'].append(com.text)
    # lis.append(data_review)

# for i in comment:
#     i = i.find('div', class_="xhr_comment_body")

# print(lis)

from flask_mysql import ConnectToDB, Test, Sach, ReviewSach
Session = ConnectToDB()
def post(data):
    try:
        session = Session()
        sach = Sach(
            sach_id= data['id'],
            title= data['title'],
            link= data['link'],
            author= data['author'],
            rate= data['rate'],
            description= data['description']
        )
        session.add(sach)
        session.commit()
        record = session.query(Sach).filter_by(sach_id= data['id']).one()
        record = record.__dict__
        if '_sa_instance_state' in record:
            del record["_sa_instance_state"]
        sach_id = record['id']
        for review in data['review']:
            review_ = ReviewSach(
                user_id= review['id_user'],
                sach_id= sach_id,
                name_user= review['name_user'],
                rate= review['rate'],
                review_content= review['review_content'],
                date_post= review['date_post']
            )
            session.add(review_)
        try:
            session.commit()
        except Exception as exp:
            print(exp)
            session.rollback()
            return 'loi1'
        return "Add AD Profile Success!"
    except Exception as exp:
        raise (exp)
        return 'loi2'
    finally:
        session.close()

# print(post(data))