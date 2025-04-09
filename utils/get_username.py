import logging

from conf.setting import USER_DATA_PATH
from utils.mysql_tool import MySqlDB
from utils.yaml_tool import read_data_from_yaml

logger = logging.getLogger(__name__)

login_data = read_data_from_yaml(USER_DATA_PATH)["login_cases"]

db = MySqlDB()


# 读取user_data yaml文件中的sql并调用sql查询方法，执行sql并返回结果

def get_username_from_db(index=0):
    try:
        # logger.info(f"logindata:{login_data}")
        # 注意：这里login_data输出的是列表，不是字典，要改为整数索引访问，列表不能用字符串索引
        sql = login_data[index]['initSql']  # 动态选择sql
        data = db.query(sql, state="all")
        # logger.info(f"查询到是数据如下：{data}")

    except KeyError as e:  # 捕获yaml错误
        logger.info(f"获取sql数据时发送错误：{e}")
        raise

    except Exception as e:  # 捕获未知错误
        logger.info(f"查询出错：{e}")
        raise

    if not data:
        logger.warning("查询未返回数据，data为空，请检查sql或数据库状态")
        return []

    return data
