import requests
import json


class SendRequests:
    def sendRequests(self, apiData, host):
        try:
            # 从读取的表格中获取响应的参数作为传递
            method = apiData["Method"]
            if host == None:
                # url = str(host) + apiData["URL"]
                url = apiData["URL"]
            else:
                url = str(host) + apiData["URL"]

            if apiData["Params"] == "":
                par = None
            else:
                par = eval(apiData["Params"])

            if apiData["Headers"] == "":
                h = None
            else:
                h = apiData["Headers"]

            if apiData["Body"] == "":
                body = None
            else:
                body = json.dumps(eval(apiData["Body"]))

            v = False

            # 发送请求
            re = requests.request(
                method=method,
                url=url,
                headers=h,
                params=par,
                json=body,
                verify=v)
            return re
        except Exception as e:
            return e


# if __name__ == '__main__':
#     host = ConfigParser(filename='conf/env.cfg')
#     env = host.get_env('env_vem_204')
#     testData = ExcelParser("D:\PycharmProjects\interfaceTest\db_fixture\InterfaceTestCases.xlsx", "Sheet2").read()
#     response = SendRequests().sendRequests(testData[0])
#     acturl_result = json.dumps(response.json())
#     print(acturl_result)
#     print("==========================")
#     expect_result = testData[0]['Expectation']
#     print(expect_result)
#     print(JsonComp(acturl_result,testData[0]['Expectation']).comp())
