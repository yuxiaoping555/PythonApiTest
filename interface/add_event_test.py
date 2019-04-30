#-*- coding:utf-8 -*-

import unittest
import requests
import os, sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from db_fixture import test_data

class Add_Event_Test(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:8000/api/add_event/"

    # 所有字段为空
    def test_add_event_all_null(self):
        payload = {
            'eid':'',
            'name':'',
            'limit':'',
            'status':'',
            'address':'',
            'start_time':''
        }
        r = requests.post(url=self.url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10021)
        self.assertEqual(self.result['message'], 'parameter error')

    # id已存在
    def test_add_event_eid_exist(self):
        payload = {
            'eid': '1',
            'name': '小米发布会',
            'limit': 2000,
            'status': 1,
            'address': '北京会议中心',
            'start_time': '2019-04-29 18:10:00'
        }
        r = requests.post(self.url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10022)
        self.assertEqual(self.result['message'], 'event id already exists')

    # 名称已存在
    def test_add_event_name_exist(self):
        payload = {
            'eid': '6',
            'name': '红米Note8',
            'limit': 2000,
            'status': 1,
            'address': '北京会议中心',
            'start_time': '2019-04-29 18:10:00'
        }
        r = requests.post(url=self.url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10023)
        self.assertEqual(self.result['message'], 'event name already exists')

    # 日期格式错误
    def test_add_event_data_type_error(self):
        payload = {
            'eid': '6',
            'name': '红米Note9',
            'limit': 2000,
            'status': 1,
            'address': '北京会议中心',
            'start_time': '2019'
        }
        r = requests.post(url=self.url, data=payload)
        self.result = r.json()
        self.assertEqual(self.result['status'], 10024)
        self.assertIn('start_time format error.', self.result['message'])


    def tearDown(self):
        print (self.result)

if __name__ == '__main__':
    test_data.init_data()
    unittest.main()