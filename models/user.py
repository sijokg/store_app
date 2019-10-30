#import sqlite3
from db import db

#class UserModel():
class UserModel(db.Model):
  __tablename__ = "users"
  
  id = db.Column(db.Integer, primary_key=True)  
  username = db.Column(db.String(80))  
  password = db.Column(db.String(80))  

  def __init__(self, username, password):
    self.username = username
    self.password = password

  @classmethod
  def find_by_username(cls, username):
    user = UserModel.query.filter_by(username=username).first()
    return user
    #connection = sqlite3.connect('code/data.db')
    #cursor = connection.cursor()
    #query = 'select * from users where username=?'
    #result = cursor.execute(query, (username,))
    #row = result.fetchone()
    #if row:
    #   user = cls(row[0], row[1], row[2])
    #else:
    #  user = None
    #connection.close()
    #return user

  @classmethod
  def find_by_id(cls, _id):
    user = cls.query.filter_by(id=_id).first()
    return user
    #connection = sqlite3.connect('code/data.db')
    #cursor = connection.cursor()
    #query = 'select * from users where id=?'
    #result = cursor.execute(query, (_id,))
    #row = result.fetchone()
    #if row:
    #   user = cls(row[0], row[1], row[2])
    #else:
    #  user = None
    #connection.close()
    #return user

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()
