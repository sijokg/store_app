import sqlite3
from flask import request
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help='This field cant be left blank'
    )
    parser.add_argument('store_id',
        type=int,
        required=True,
        help='Every item needs a store id'
    )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {"message": "Item not found"}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
          return {"message": "The item {} already exists".format(name)}

        data = Item.parser.parse_args()
        #item = Item{'name': name, 'price': data['price']}
        item = ItemModel(name, data['price'], data['store_id'])
        try:
            #ItemModel.insert(item)
            #item.insert()
            item.save_to_db()
        except:
            return {"message": "There was a problem happened inserting record to database"}, 500
        return item.json(), 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_record()
        #connection = sqlite3.connect('data.db')
        #cursor = connection.cursor()
        #query = 'delete from items where name=?'
        #cursor.execute(query, (name,))
        #connection.commit()
        #connection.close()
        return {'messgage': 'Item is deleted'}

    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item is None:
            item = ItemModel(name, data['price'])
        else:
            item.price = data['price']
        item.save_to_db()
        return item.json()
        #updated_item = {"name": name, "price": data['price']}
        #updated_item = ItemModel(name, data['price'])
        #if item is None:
            #try:
                #ItemModel.insert(updated_item)
                #updated_item.insert()
            #except:
            #    return {"message": "Some error happened while creating record"}, 500
        #else:
            #try:
                #ItemModel.update(updated_item)
                #updated_item.update()
            #except:
            #    return {"message": "some error happened while updating record"}, 500
        #return updated_item.json()
        #return item.json()


class ItemList(Resource):
    def get(self):
        return {"items": [item.json() for item in ItemModel.query.all()]}
        #The following line is same as above line
        #return {"items": list(map(lambda x: x.json(), ItemModel.query.all()))}

        #connection = sqlite3.connect('code/data.db')
        #cursor = connection.cursor()
        #query = 'select * from items'
        #result = cursor.execute(query)
        #items = []
        #for row in result:
        #    items.append({"id": row[0], "name": row[1], "price": row[2]})
        #connection.commit()
        #connection.close()
        #return {"items": items}
