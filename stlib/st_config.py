# 处理ini配置文件

import configparser
import os

try:
    from .st_settings import DEFAULT_CONFIG, DEFAULT_INI_NAME
except Exception:
    from st_settings import DEFAULT_CONFIG, DEFAULT_INI_NAME


class CONFIG(object):
    version = "1.0.0"
    default_config = DEFAULT_CONFIG
    default_name = DEFAULT_INI_NAME

    def __init__(self, work_dir, file=""):
        self.file = file if file else self.default_name
        self.work_dir = work_dir
        self.fullpath = os.path.join(self.work_dir, self.file)
        self.config = self.default_config
        self._reset()

    def _reset(self):
        self.con = configparser.ConfigParser()
        # self.con.optionxform = str  # 保持获取的键原样。否则全为小写

    def get(self):
        if os.path.isfile(self.fullpath):
            # 存在配置文件，读取并赋值
            self.con.read(self.fullpath, encoding="utf-8")
            for section in self.con.sections():
                options = self.con.items(section)
                self.config[section] = {}
                for k, v in options:
                    self.config[section][k] = v
        else:
            # 不存在配置文件，建个新的
            self.create_new()
        return self.config

    def save(self, dic):
        self._reset()
        self.con.read_dict(dic)
        self._save_file()

    def create_new(self):
        self._reset()
        self.con.read_dict(self.default_config)
        self._save_file()

    def _save_file(self):
        with open(self.fullpath, "w", encoding="utf-8") as fp:
            self.con.write(fp)
