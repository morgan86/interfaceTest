import requests
import unittest
from ddt import ddt, data, unpack
from common.Logit import exception, create_logger
from common.ExcelParser import ExcelParser


@ddt
class Test(unittest.TestCase):
    logger = create_logger()
    testData = ExcelParser("db_fixture/InterfaceTestCases.xlsx",
                           "Sheet1").read()

    def __init__(self,
                 method=None,
                 url=None,
                 payload=None,
                 headers=None,
                 querystring=None):
        self.method = method
        self.url = url
        self.payload = payload
        self.headers = headers
        self.querystring = querystring

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @exception(logger)
    @data(testData)
    def test_get(self):
        r = requests.request(
            "GET",
            self.url,
            data=self.payload,
            headers=self.headers,
            querystring=self.querystring)
        response = r.json()
        self.assertEqual(response, )

    def test_put(self):
        pass
        # requests.request("GET", url, headers=headers, params=querystring)
        # requests.request("PUT", url, data=payload, headers=headers)

    def test_post(self):
        pass
        # requests.request("POST", url, data=payload, headers=headers)  # raw text
        # requests.request("POST", url, data=payload, headers=headers)  # form data
        # requests.request("POST", url, data=payload, headers=headers, params=querystring)

    def test_del(self):
        pass
        # requests.request("DELETE", url, data=payload, headers=headers)

    method_dict = {
        "GET": test_get,
        "PUT": test_put,
        "POST": test_post,
        "DELETE": test_del,
    }

    # if self.method in method_dict.keys():
    #     method_dict[read_from_xls_method]()
    # else:
    #     print('Unsupport request methods!')


if __name__ == "__main__":
    # Initial data
    p1 = ExcelParser(
        filename='InterfaceTestCases.xlsx', filepath='../db_fixture/')

    # Initial test
    url = p1.get_cell(2, 4)
    querystring = p1.get_cell(2, 6)
    method = p1.get_cell(2, 5)
    t1 = Test(method, url, querystring)
    Test.method_dict[method]()

import HtmlTestRunner
import unittest


class TestStringMethods(unittest.TestCase):
    """ Example test for HtmlRunner. """

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOo'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_error(self):
        """ This test should be marked as error one. """
        raise ValueError

    def test_fail(self):
        """ This test should fail. """
        self.assertEqual(1, 2)

    @unittest.skip("This is a skipped test.")
    def test_skip(self):
        """ This test should be skipped. """
        pass


if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output='test_report', report_title="test123"))

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format=
    '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    filename='logs/test.log',
    filemode='w')

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')

import logging
import functools


def create_logger():
    """
    Creates a logging object and returns it
    """
    logger = logging.getLogger("example_logger")
    logger.setLevel(logging.INFO)
    # create the logging file handler
    fh = logging.FileHandler(r"logs/test1.log")
    fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    formatter = logging.Formatter(fmt)
    fh.setFormatter(formatter)
    # add handler to logger object
    logger.addHandler(fh)
    return logger


# logger = create_logger()


def exception(logger):
    """
    A decorator that wraps the passed in function and logs
    exceptions should one occur

    @param logger: The logging object
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except:
                # log the exception
                err = "There was an exception in  "
                err += func.__name__
                logger.exception(err)

            # re-raise the exception
            raise

        return wrapper

    return decorator


@exception(create_logger())
def zero_divide():
    1 / 0


if __name__ == '__main__':
    zero_divide()

#
# def makebold(fn):
#     def wrapped(*args, **kwargs):
#         return "<b>" + fn(*args, **kwargs) + "</b>"
#
#     return wrapped
#
#
# def makeitalic(fn):
#     def wrapped(*args, **kwargs):
#         return "<i>" + fn(*args, **kwargs) + "</i>"
#
#     return wrapped
#
#
# @makebold
# @makeitalic
# def hello(s):
#     return "hello world" + s
#
#
# print(hello('test'))
