import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,create_engine,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship

Base = declarative_base()
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/mydatabase',echo=True)
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    nickname= Column(String(50))
    def __repr__(self):
        return "<User(name='%s', fullname='%s', \
            nickname='%s')>" % (self.name, self.fullname, self.nickname)


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String(50), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="addresses")
    def __repr__(self):
         return "<Address(email_address='%s')>" % self.email_address

User.addresses = relationship("Address", order_by=Address.id, back_populates="user")


Base.metadata.create_all(engine)
ed_user = User(name='et',fullname='Ed Jones',nickname='esjone')
ed_user = session.add(ed_user)
our_user = session.query(User).filter_by(name='et').order_by(User.id.desc())[1:3]


print(session.new)
session.rollback()
session.commit()
# print(our_user)


for name, fullname in session.query(User.name, User.fullname).order_by(User.id.desc())[1:3]:
    print(name, fullname)