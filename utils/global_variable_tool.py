import logging

logger = logging.getLogger(__name__)


class GlobalVariable(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls, *args)
        return cls.__instance

    def __init__(self):
        self.globalVars = {}
        #self.res = []

    def setVar(self,key,value):
        self.globalVars[key] = value

    # 获取某个全局变量
    def getVar(self, key,default=None):
        return self.globalVars.get(key,default)

    # 获取全部全局变量
    def getVars(self):
        return self.globalVars

    # 删除某个全局变量
    def deleteVar(self,key):
        self.globalVars.pop(key)

    # 删除全局变量
    def deleteVar(self):
        self.globalVars


    # 清空全局变量
    def cleanVars(self):
        self.globalVars.clear()

global_var = GlobalVariable()