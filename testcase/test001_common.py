from public import Api
import json
import unittest
import urllib3
urllib3.disable_warnings()  # 禁用安全请求警告

cheese = Api()
class Cheese_common_test(unittest.TestCase):
    '''
    Cheese_common接口用例
    '''
    def setUp(self):
        input(0)

    def tearDown(selfs):
        input(1)

    def test01_common_content_config(self):
        '''
        用例：common/content_config
        '''
        r = cheese.content_config("en-US","1.12","13.3.1","IPhone 7s")
        re = r.json()
        self.assertEqual(re["success"], "断言失败")

    def test02_common_banner(self):
        r = cheese.banner()
        re = r.json()
        self.assertEqual(re["success"], "断言失败")