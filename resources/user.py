import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):

  parser = reqparse.RequestParser()
  parser.add_argument('username',
    type=str,
    required=True,
    help='This field cant be left blank'
  )
  parser.add_argument('password',
    type=str,
    required=True,
    help='This field cant be left blank'
  )

  def post(self):
    data = UserRegister.parser.parse_args()
    if UserModel.find_by_username(data['username']):
      return {'message': 'The same user already exists'}, 400
    user = UserModel(data['username'], data['password'])
    user.save_to_db()
    #connection = sqlite3.connect('code/data.db')
    #cursor = connection.cursor()
    #query = 'insert into users values (NULL, ?, ?)'
    #cursor.execute(query, (data['username'], data['password']))
    #connection.commit()
    #connection.close()

    return {'message': 'User is created'}
