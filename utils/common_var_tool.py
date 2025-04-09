from conf.setting import VAR_DATA_PATH
from utils.yaml_tool import read_data_from_yaml
import logging

logger = logging.getLogger(__name__)


def load_common_var():
    cv = read_data_from_yaml(VAR_DATA_PATH)
    # logger.info("常用变量：{}".format(cv))
    return cv


'''

def get_common_var():
    return load_common_var()'''
