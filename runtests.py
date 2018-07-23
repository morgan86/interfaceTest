from HTMLTestRunner import *
import time
import unittest

# 指定测试用例为当前文件夹下的 testcases 目录
test_dir = '../interfaceTest'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='testcase.py')

if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d-%H_%M_%S")
    filename = now + '_result.html'
    with open('reports/' + filename, encoding='utf-8', mode='w') as fp:
        runner = HTMLTestRunner(
            stream=fp, title='自助售货机云平台运维开发-测试报告', description='详细执行结果如下： ')
        runner.run(discover)
