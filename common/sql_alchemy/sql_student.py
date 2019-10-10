from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
# engine = create_engine('sqlite:///college.db', echo = True)
engine = create_engine('mysql+pymysql://root:123456@localhost:3306/mydb',echo=False)

meta = MetaData()

students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String(50)), 
   Column('lastname', String(50)),
)

meta.create_all(engine)

print('ok')
