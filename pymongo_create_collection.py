import pymongo
import datetime


# Подключаемся к инстансу MongoDB
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]


# Создаём объект коллекции Account
mycol = mydb["Account"]


# Формируем контент для записи в коллекцию:
users = [{
             'number': '7800000000000',
             'name': 'Пользователь №',
             'sessions': [
             {
                 'created_at': '2016-01-01T00:00:00',
                 'session_id': '6QBnQhFGgDgC2FDfGwbgEaLbPMMBofPFVrVh9Pn2quooAcgxZc',
                 'actions': [
                 {
                     'type': 'read',
                     'created_at': '2017-01-01T01:20:01',
                 },
                 {
                     'type': 'read',
                     'created_at': '2018-01-01T01:21:13',
                 },
                 {
                     'type': 'create',
                     'created_at': '2016-01-01T01:33:59',
                 }
                 ],
             }
             ]
          },
          {
             'number': '7800000000001',
             'name': 'Пользователь №',
             'sessions': [
             {
                 'created_at': '2016-01-01T00:00:00',
                 'session_id': '6QBnQhFGgDgC2FDfGwbgEaLbPMMBofPFVrVh9Pn2quooAcgxZb',
                 'actions': [
                 {
                     'type': 'update',
                     'created_at': '2018-01-01T01:20:01',
                 },
                 {
                     'type': 'update',
                     'created_at': '2016-01-01T01:21:13',
                 },
                 {
                     'type': 'create',
                     'created_at': '2017-01-01T01:33:59',
                 }
                 ],
             }
             ]
          },
          {
             'number': '7800000000002',
             'name': 'Пользователь №',
             'sessions': [
             {
                 'created_at': '2016-01-01T00:00:00',
                 'session_id': '6QBnQhFGgDgC2FDfGwbgEaLbPMMBofPFVrVh9Pn2quooAcgxZd',
                 'actions': [
                 {
                     'type': 'read',
                     'created_at': '2016-01-01T01:20:01',
                 },
                 {
                     'type': 'update',
                     'created_at': '2016-01-01T01:21:13',
                 },
                 {
                     'type': 'delete',
                     'created_at': '2018-01-01T01:33:59',
                 }
                 ],
             }
             ]
          }
         ]


for u in users:
    print("========INSERT DOCUMENT:========")
    x = mycol.insert_one(u)
    print(x)
    print(x.inserted_id)


# Проверяем список коллекций в бд
print("========COLLECTIONS IN DB========")
print(mydb.list_collection_names())

# Проверяем, создана ли коллекция пользователей Account
collist = mydb.list_collection_names()
if "Account" in collist:
      print("====SUCCESS: ACCOUNT COLLECTION CREATED====")
else:
      print("====ERROR: FAIL TO CREATE ACCOUNT COLLECTION====")
