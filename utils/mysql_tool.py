import pymysql
import logging

logger = logging.getLogger(__name__)
from conf.setting import mysql_info


class MySqlDB:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls, *args)
        return cls.__instance

    def __init__(self):
        try:
            self.conn = pymysql.connect(
                host="192.168.117.180",
                port=mysql_info["port"],
                user=mysql_info["user"],
                password=mysql_info["password"],
                db=mysql_info["db"],
                charset=mysql_info["charset"]
         )

            # 使用cursor方法获取操作游标
            self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        except pymysql.MySQLError as e:
            logger.error(f"MySQL 连接失败: {e}")
            raise

        except Exception as ex:
            logger.error(f"未知错误: {ex}")
            raise

    def __del__(self):
        try:
            self.cur.close()
            self.conn.close()
        except Exception as ex:
            logger.error(f"出错了：{ex}")

    def query(self, sql, state="all"):
        try:

            self.cur.execute(sql)
            if state == "all":
                data = self.cur.fetchall()
            else:
                data = self.cur.fetchone()
            return data
        except Exception as ex:
            logger.error(f"出错了：{ex}")
            raise

    def execute(self, sql):
        try:
            rows = self.cur.execute(sql)
            self.conn.commit()
            return rows
        except Exception as ex:
            logger.error(f"出错了：{ex}")
            self.conn.rollback()
            raise


if __name__ == '__main__':
    pass
