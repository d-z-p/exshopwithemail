import xlrd  # excel的读取  xlrd目前支持(2007版)与xls(2003版)
import xlsxwriter
import xlwt
from xlutils.copy import copy

"""
读取：xlrd   写入：xlsxwriter  修改（追加写入）：xlutils
"""


def setStyle(name, height, color, bold=False):
    style = xlwt.XFStyle()  # 初始化样式
    font = xlwt.Font()  # 为样式创建字体
    font.name = name  # 字体类型：比如宋体、仿宋也可以是汉仪瘦金书繁
    font.colour_index = color  # 设置字体颜色
    font.height = height  # 字体大小
    style.font = font  # 定义格式

    alignment = xlwt.Alignment()
    alignment.horz = xlwt.Alignment.HORZ_CENTER
    alignment.vert = xlwt.Alignment.VERT_CENTER
    # alignment.horz = color

    style.alignment = alignment
    return style  # 返回样式


def write_excel_xls_append(excel_w, result_w):
    path = r"F:\课程课件\05.Python\TS\day8_1\TestCaseExcel\测试用例.xls"  # 定义文件路径
    workbook = xlrd.open_workbook(path, formatting_info=True)  # 打开工作簿 # 打开工作簿，formatting_info样式不变的情况下。
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    # worksheet = workbook.sheet_by_name(sheets[0]) # 获取工作簿中所有表格中的的第一个表格
    # rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数

    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格

    # 追加写入数据  参数对应：行，列，值，setStyle字体样式(可以没有)
    # new_worksheet.write(excel_w, 9, result_w)
    new_worksheet.write(excel_w, 9, result_w, setStyle('宋体', 400, 2, False))
    new_workbook.save(path)  # 保存工作簿

    # 提示写入数据成功
    # print("xls格式表格【追加】写入数据成功！")

    # write_excel_xls_append(1,"pass")

































    # https://www.cnblogs.com/xiaodingdong/p/8012282.html 可以去参考
