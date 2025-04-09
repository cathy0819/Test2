
from utils.read_file_tools.yaml_control import GetYamlData
from conf.setting import ensure_path_sep
from utils.other_tools.models import Config


_data = GetYamlData(ensure_path_sep("\\conf\\config.yaml")).get_yaml_data()
config = Config(**_data)

