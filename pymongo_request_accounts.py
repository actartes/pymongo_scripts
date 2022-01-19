import sys
import json
import pymongo
import datetime


def get_isodate(date):
    '''
    Перевод даты из ISODate в нужный формат
    '''
    if date == None: date = "0001-01-01T00:00:00"
    return(datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S"))




# Подключаемся к инстансу MongoDB
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

# Создаём объект коллекции Account
mycol = mydb["Account"]

# Проверяем, есть ли коллекция Account в базе
collist = mydb.list_collection_names()
if "Account" in collist:
    print("====ACCOUNT COLLECTION EXISTS====")
else:
    sys.exit(1)    
 


docs_total = []
# Получение документов из базы
for doc in mydb.Account.find():
    # Извлечение списка действий из документа
    actions_total = []
    for session in doc["sessions"]:
        actions_total = actions_total + [a for a in session["actions"]]

    # Формирование итогового списка действий
    actions_final = []
    types = ["create", "read", "update", "delete"]
    for t in types:
        count = 0
        last = None

        # Подсчёт количества действий по типам,
        # запоминание даты последнего
        for action in actions_total:
            if action["type"] == t:
                count += 1
                if last == None: last = action["created_at"]
                if get_isodate(action["created_at"]) > get_isodate(last):
                    last = action["created_at"]  

        actions_final.append({"type": t, "count": count, 'last': last})

    # Сортировка итового списка действий по дате последнего
    actions_sorted = sorted(actions_final,
                            key=lambda action: get_isodate(action["last"]),
                            reverse=True)

    docs_total.append({"number": doc["number"], "actions": actions_sorted})

print(json.dumps(docs_total, indent=4, sort_keys=True))
