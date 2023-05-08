from database import init_db, db_session
from models import *

init_db()

user1 = User(username="a", password="123")
db_session.add(user1)
db_session.commit()