import xlrd


class ExcelParser:
    """
    s = ExcelParser("D:\PycharmProjects\interfaceTest\db_fixture\InterfaceTestCases.xlsx","Sheet1").read()
    print(s)
    """

    def __init__(self, filename=None, sheetname=None):
        self.filename = filename
        self.sheetname = sheetname

    def read(self):
        data = xlrd.open_workbook(self.filename)
        table = data.sheet_by_name(self.sheetname)

        # 获取总行数、总列数
        nrows = table.nrows
        ncols = table.ncols
        if nrows > 1:
            # 获取第一行标题的内容，列表格式
            keys = table.row_values(0)

            listApiData = []
            # 获取每一行的内容，列表格式
            for col in range(1, nrows):
                values = table.row_values(col)
                # keys，values这两个列表一一对应来组合转换为字典
                # 挑选激活案例
                if str(values[-1]).lower() == 'y':
                    api_dict = dict(zip(keys, values))
                    listApiData.append(api_dict)
            return listApiData
        else:
            print("表格未填写数据")
            return None


# if __name__ == '__main__':
#     s = ExcelParser("D:\PycharmProjects\interfaceTest\db_fixture\InterfaceTestCases.xlsx", "Sheet1").read()
#     print("list: %s \n length is " % s, len(s))
#     for i in s:
#         print(i)
