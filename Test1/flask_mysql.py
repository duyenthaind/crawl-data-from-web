from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import *
from sqlalchemy.orm import *
from sqlalchemy import *

Base = declarative_base()


# khoi tao ket noi vao co so du lieu
def ConnectToDB():
	engine = create_engine('mysql+mysqldb://root:vjpvjp123A01@localhost/test1_crawlData?charset=utf8mb4')
	Session = sessionmaker(bind=engine)
	return Session

class Test(Base):
	__tablename__ = 'test'
	id = Column(Integer, primary_key=True)
	name = Column(String)

class Sach(Base):
	__tablename__ = 'sach'
	id = Column(Integer, primary_key=True)
	sach_id = Column(Integer)
	title = Column(String)
	link = Column(String)
	author = Column(String)
	rate = Column(Float)
	description = Column(String)
	review = relationship('ReviewSach')

class ReviewSach(Base):
	__tablename__ = 'review_sach'
	id = Column(Integer, primary_key=True)
	user_id = Column(Integer)
	sach_id = Column(Integer, ForeignKey('sach.id'))
	name_user = Column(String)
	rate = Column(Integer)
	review_content = Column(String)
	date_post = Column(String)
