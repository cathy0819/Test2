import logging
import re
import json

from conf.setting import VAR_DATA_PATH, PATTERN
from utils.yaml_tool import read_data_from_yaml
from utils.common_var_tool import load_common_var
from utils.global_variable_tool import GlobalVariable

logger = logging.getLogger(__name__)

global_var = GlobalVariable()



def var_substitution(param):

    param = json.dumps(param) if not isinstance(param, str) else param

    var_dic = load_common_var()  # 加载常用变量字典
    logger.info("常用变量字典: {}".format(var_dic))


    for key, value in var_dic.items():
        if key in param:
            param = param.replace(key, str(value))  # 替换内容

    try:
        param = json.loads(param)  # 确保替换后保持 JSON 格式
    except json.JSONDecodeError as e:
        logger.error("替换后数据非合法 JSON 格式: {}".format(param))
        raise e

    return param

'''def var_substitution(param):
    """
    递归替换字典/列表中包含的变量标识符
    :param data: 原始数据（可以是字典、列表、字符串）
    :return: 替换后的数据
    """
    var_dic = load_common_var()  # 加载变量字典
    logger.info("常用变量字典: {}".format(var_dic))

    if isinstance(param, dict):  # 如果是字典，递归处理
        for key, value in param.items():
            param[key] = var_substitution(value)
    elif isinstance(param, list):  # 如果是列表，递归处理
        for index, item in enumerate(param):
            param[index] = var_substitution(item)
    elif isinstance(param, str):  # 如果是字符串，进行变量替换
        for var_key, var_value in var_dic.items():
            if var_key in param:
                param = param.replace(var_key, str(var_value))
    return param'''




'''添加替换依赖参数的方法'''


def parameter_substitution(param):

    param = json.dumps(param) if not isinstance(param, str) else param

    keys = re.findall(PATTERN, param)
    print(keys)

    for key in keys:
        value = global_var.getVar(key)
        if value is None:
            logger.info(f"全局变量{key} 获取失败")
        else:
            logger.info(f"全局变量 {key} = {value}")
        param = param.replace('${' + key + '}', str(value))  # replace 后返回替换的字符串
    return param


'''def parameter_substitution(data):
    """
    处理 ${var} 格式的变量（从全局变量获取）
    支持嵌套数据结构（字典/列表）
    """
    if isinstance(data, dict):
        return {k: parameter_substitution(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [parameter_substitution(item) for item in data]
    elif isinstance(data, str):
        # 匹配 ${var} 格式
        return re.sub(
            r'\$\{(\w+)\}',
            lambda m: str(gv.getVar(m.group(1), m.group(0))),
            data
        )
    return data'''


