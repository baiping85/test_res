import time
import unittest
import sys
sys.path.append('C:\\Users\\baiping\\PycharmProjects\\untitled1')
from HTMLTestRunner import HTMLTestRunner

from ddt import ddt, data, unpack, file_data


@ddt
class MyTestCase(unittest.TestCase):


    # @data(['user','name'],['admin','4444'])
    # @unpack
    @file_data('login_data.yaml')
    def test_1_case(self,**user_data):
        # print(time.localtime())
        # date_now = time.strftime('%Y-%m-%d', time.localtime())
        print(date_now)
        print(user_data)


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    test_case=unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    suite.addTests(test_case)
    #获取当前时间
    date_now=time.strftime('%Y-%m-%d',time.localtime())
    #创建HTML报告
    with open('report_'+date_now+'.html','wb+') as file:
        runner=HTMLTestRunner(stream=file, verbosity=1, title='auto_test', description='ui_auto_test')
        runner.run(suite)