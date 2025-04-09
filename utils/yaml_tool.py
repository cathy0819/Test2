import yaml
import logging

logger = logging.getLogger(__name__)


# 读取yaml中的用例/变量数据
def read_data_from_yaml(file_path):
    try:
        f = open(file_path, "r", encoding="utf-8")  # 打开指定路径的文件 file_path，以只读模式 ("r") 读取文件内容
        res = yaml.load(f, yaml.FullLoader)  # YAML 文件的内容解析为相应的 Python 数据结构
        return res
    except Exception as e:
        logger.error(f"加载yaml出错：{e}")
        raise
