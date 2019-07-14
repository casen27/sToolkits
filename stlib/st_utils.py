# 扩展工具相关类

import hashlib
import json
import os
import time

import pyperclip


class CalcFileHash(object):
    version = "1.0.0"
    _all_hashes = {"md5", "sha1", "sha256", "sha384", "sha512"}

    def __init__(self, file, workDir=None):
        self.file = file
        self.workDir = workDir
        self._basic = {}
        self._hashes = {}

    def _get_basic(self):
        path, name = os.path.split(self.file)
        self._basic = {}
        self._basic["file"] = self.file
        self._basic["path"] = path
        self._basic["name"] = name
        self.stat = os.stat(self.file)
        self._basic["size"] = format(self.stat.st_size, ",")
        self._basic["atime"] = self._strftime(self.stat.st_atime)
        self._basic["mtime"] = self._strftime(self.stat.st_mtime)
        self._basic["ctime"] = self._strftime(self.stat.st_ctime)

    def _strftime(self, timestamp):
        # 时间戳转化为年月日时分秒
        lt = time.localtime(timestamp)
        st = time.strftime("%Y/%m/%d %H:%M:%S", lt)
        return st

    def basic(self):
        self._get_basic()
        return self._basic

    def hashes(self, needhash):
        for hash in needhash:
            if hash in self._all_hashes:
                if self._hashes.get(hash):
                    continue  # 已经计算过了
                self._hashes[hash] = self._calc_hash(hash)
        return self._hashes

    def _calc_hash(self, type):
        try:
            with open(self.file, "rb") as fo:
                value = hashlib.new(name=type, data=fo.read()).hexdigest()
            return value
        except:  # 文件不存在、文件打不开、传参数错误
            return ""

    def copytext(self):
        data = []
        for k, v in self._basic.items():
            line = "【" + k + "】" + v + "\n"
            data.append(line)
        for k, v in self._hashes.items():
            line = "【" + k + "】" + v + "\n"
            data.append(line)
        data2 = "".join(data)
        pyperclip.copy(data2)
        # print(data2)

    def copyjson(self):
        data = {**self._basic, **self._hashes}
        data2 = json.dumps(data, ensure_ascii=False, indent=4)
        # print(data2)
        pyperclip.copy(data2)


class PicMixZip(object):
    version = "1.0.0"
    _pics = {".png", ".jpg", ".jpeg", ".bmp"}
    _zips = {".zip", ".rar"}

    def __init__(self, pic, zip, store):
        self._pic = pic
        self._zip = zip
        self._store = store

    def _check(self):
        pass
        # 检测文件是否存在，检测类型
        # os.path.isfile(self._pic)
        # 检测输出文字是否与已有文件冲突

    def run(self):
        self.mix()

    def mix(self):
        with open(self._pic, "rb") as fpic:
            p = fpic.read()
        with open(self._zip, "rb") as fzip:
            z = fzip.read()
        with open(self._store, "wb") as fp:
            fp.write(p)
            fp.write(z)

