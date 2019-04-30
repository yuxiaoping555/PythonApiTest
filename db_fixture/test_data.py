import sys
sys.path.append('../db_fixture')

from db_fixture.mysql_db import DB

datas = {
    'sign_event':[
        {'id': 1, 'name': '红米Note8', '`limit`': 2000, 'status': 1, 'address': '北京鸟巢1',
         'start_time': '2019-09-26 00:10:00', 'create_time': '2019-04-29 17:13:00'},

        {'id': 2, 'name': '可参加人数为0', '`limit`': 0, 'status': 1, 'address': '北京鸟巢1',
         'start_time': '2019-09-26 00:10:00', 'create_time': '2019-04-29 17:13:00'},

        {'id': 3, 'name': '当前状态为0 关闭', '`limit`': 2000, 'status': 0, 'address': '北京鸟巢1',
         'start_time': '2019-09-26 00:10:00', 'create_time': '2019-04-29 17:13:00'},

        {'id': 4, 'name': '发布会已经结束', '`limit`': 2000, 'status': 1, 'address': '北京鸟巢1',
         'start_time': '2010-09-26 00:10:00', 'create_time': '2010-04-29 17:13:00'},

        {'id': 5, 'name': '小米5发布会', '`limit`': 2000, 'status': 1, 'address': '北京国家会议中心',
         'start_time': '2019-09-26 00:10:00', 'create_time': '2019-04-29 17:13:00'}
    ],

    'sign_guest':[
        {'id':1, 'realname': 'alen', 'phone': 16601010100, 'email':'alen@mail.com', 'sign':0, 'create_time': '2019-04-29 17:13:00','event_id':1},
        {'id':2, 'realname': 'has sign', 'phone': 16601010101, 'email':'sign@mail.com', 'sign':0, 'create_time': '2019-04-29 17:13:00','event_id':1},
        {'id':3, 'realname': 'tom', 'phone': 16601010102, 'email':'tom@mail.com', 'sign':0, 'create_time': '2019-04-29 17:13:00','event_id':5}
    ]
}


def init_data():
    db = DB()
    for table, data in datas.items():
        db.clear(table)
        for d in data:
            db.insert(table, d)
    db.close()

if __name__ == '__main__':
    init_data()