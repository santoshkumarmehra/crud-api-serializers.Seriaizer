import requests
import json

url = "http://127.0.0.1:8000/studentapi/"

def get_data(id=None):
    data = {}
    if data is not None:
        data['id'] = id
    json_data = json.dumps(data)
    res=requests.get(url=url, data=json_data)
    data = res.json()
    print(data)

# get_data(1)


def post_data():
    data={
        'name':'saa',
        'roll':12,
        'city':'jai'
    }
    json_data = json.dumps(data)
    r = requests.post(url=url, data=json_data)
    data = r.json()
    print(data)

# post_data()

def update_data():
    data={
        'id':1,
        'name':'samy',
        'city':'januu'
    }
    json_data = json.dumps(data)
    r = requests.put(url=url, data=json_data)
    data = r.json()
    print(data)

# update_data()


def delete_data():
    data={
        'id':1,
    }
    json_data = json.dumps(data)
    r = requests.delete(url=url, data=json_data)
    data = r.json()
    print(data)

delete_data()
