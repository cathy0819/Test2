import logging
import os.path
import os
from typing import Text

logger = logging.getLogger(__name__)

# 获取项目路径
# __file__表示当前运行的python的路径。
# 使用 os.path.abspath(__file__) 可以转换为绝对路径，确保文件路径在跨平台或不同运行环境下能正确解析
# os.path.dirname(path)：返回传入路径的父目录，这里两次调用
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 定义测试用例数据文件路径
# 用于安全地拼接路径部分，避免直接使用字符串拼接可能引起的路径错误
# 拼接出 case.yaml 文件的绝对路径，这通常用于项目中根据文件路径加载数据
USER_DATA_PATH = os.path.join(BASE_PATH, 'data', 'user_data.yaml')
OTR_DATA_PATH = os.path.join(BASE_PATH, 'data', 'OTR.yaml')
PCASE_DATA_PATH = os.path.join(BASE_PATH, 'data', 'product_data.yaml')
UPDATE_DATA_PATH = os.path.join(BASE_PATH, 'data', 'update_order.yaml')

# 定义常用变量的数据文件路径
VAR_DATA_PATH = os.path.join(BASE_PATH, 'data', 'variable.yaml')

ENV_HOST_PORT = 'https://aspm-qa.mercedes-benz.com.cn'
PATTERN = r'\$\{(\w+)\}'

    #'\$\{(.*?)\}'



def root_path():
    """ 获取当前文件所在文件夹的路径，并取上一层目录路径, os.path.abspath将__file__转换为绝对路径。"""
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return path


def ensure_path_sep(path: Text) -> Text:
    """兼容 windows 和 linux（/） 不同环境的操作系统路径 .返回路径是完整路径——即会拼接项目的根路径 (root_path) 和传递的路径参数"""
    if "/" in path:
        path = os.sep.join(path.split("/"))

    if "\\" in path:
        path = os.sep.join(path.split("\\"))

    return root_path() + path


mysql_info = {
    "host": "192.168.117.180",
    "port": 3306,
    "user": "root",
    "password": "qzcsbj",
    "db": "qzcsbj",
    "charset": "utf8"
}
