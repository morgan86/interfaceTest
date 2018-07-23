from ddt import ddt, data
from sendrequest import SendRequests
from common.excelparser import ExcelParser
from common.logit import *
from common.configfileparser import ConfigFileParser
import json
import unittest

testData = ExcelParser("db_fixture/InterfaceTestCases.xlsx", "Sheet2").read()
logger = create_logger()
m = ConfigFileParser(filename='D:\PycharmProjects\interfaceTest\conf\env.cfg')
HOST = m.get_value('env_test', 'host')

@ddt
class Test1(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(*testData)
    @exception(logger)
    def test_api(self, data):
        response = SendRequests().sendRequests(data, host=HOST)

        acturl_result = json.dumps(response.json())
        expect_result = data['Expectation']
        self.assertEqual(acturl_result, expect_result)


# if __name__ == '__main__':
#     unittest.main()
