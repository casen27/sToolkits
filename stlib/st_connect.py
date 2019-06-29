"""
使用库  https://github.com/Baidu-AIP/python-sdk
安装源  pip install git+https://github.com/Baidu-AIP/python-sdk.git@master
"""
import hashlib
import json
import os
import time

import requests
from aip import AipSpeech


class ConnectBaidu(object):
    # 链接测试网络状况、账号密码是否可用
    @classmethod
    def connect1(cls, auths):
        # 测试链接：语音转文字、文字转语音、图片OCR
        try:
            sy = Synthesis(auths,"百度")
            result = sy.run()
        except Exception as e:
            result = {}
            # print(e)
        if isinstance(result, dict):
            # 链接失败
            return False
        else:
            # 链接成功，声音的二进制文件
            return True

    @classmethod
    def connect2(cls, auths):
        # 测试链接：翻译
        try:
            t = Translate(auths=auths, text="English")
            result = t.run()
        except Exception as e:
            result = ""
            # print(e)
        if result == "英语":
            return True
        else:
            return False


class ASR(object):
    # 声音文件转字符串
    def __init__(self, workDir, file, auths):
        self.workDir = workDir
        self.file = file
        self.auths = {}
        self.auths["appId"] = auths["appid"]
        self.auths["apiKey"] = auths["apikey"]
        self.auths["secretKey"] = auths["secretkey"]
        self.client = AipSpeech(**self.auths)

    def run(self):
        with open(self.file, 'rb') as fp:
            rb = fp.read()
        ext = os.path.splitext(self.file)[1].lstrip(".")
        datas = self.client.asr(rb, ext)
        # print(datas)
        if datas.get("err_msg") == "success.":
            res = datas.get("result", "")
            str0 = res[0]
        else:
            str0 = json.dumps(datas, ensure_ascii=False)
        # print(str0)
        return str0


class Synthesis(object):
    # 字符串合成语音文件

    """
    options参数    可需  描述
    tex  必填  合成的文本，使用UTF-8编码。小于2048个中文字或者英文数字。（文本在百度服务器内转换为GBK后，长度必须小于4096字节）
    tok  必填  开放平台获取到的开发者access_token（见上面的“鉴权认证机制”段落）
    cuid  必填  用户唯一标识，用来计算UV值。建议填写能区分用户的机器 MAC 地址或 IMEI 码，长度为60字符以内
    ctp  必填  客户端类型选择，web端填写固定值1
    lan  必填  固定值zh。语言选择,目前只有中英文混合模式，填写固定值zh
    spd  选填  语速，取值0-15，默认为5中语速
    pit  选填  音调，取值0-15，默认为5中语调
    vol  选填  音量，取值0-15，默认为5中音量
    per  选填  发音人选择, 0为普通女声，1为普通男生，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女声
    aue  选填  3为mp3格式(默认)； 4为pcm-16k；5为pcm-8k；6为wav（内容同pcm-16k）; 注意aue=4或者6是语音识别要求的格式，但是音频内容不是语音识别要求的自然人发音，所以识别效果会受影响。

    """

    def __init__(self, auths, text, options={}):
        self.auths = {}
        self.auths["appId"] = auths["appid"]
        self.auths["apiKey"] = auths["apikey"]
        self.auths["secretKey"] = auths["secretkey"]
        # print(self.auths)
        self.client = AipSpeech(**self.auths)
        self.text = text
        self.options = options
        self.options2 = {}
        self._check_options()

    def _check_options(self):
        for k, v in self.options.items():
            if k == "spd":  # 语速
                if v in range(0, 16):
                    self.options2[k] = v
                else:
                    self.options2[k] = 5
            elif k == "pit":  # 音调
                if v in range(0, 16):
                    self.options2[k] = v
                else:
                    self.options2[k] = 5
            elif k == "vol":  # 音量
                if v in range(0, 16):
                    self.options2[k] = v
                else:
                    self.options2[k] = 5
            elif k == "per":  # 发音人员
                if v in [0, 1, 3, 4]:
                    self.options2[k] = v
                else:
                    self.options2[k] = 0
            elif k == "aue":  # 声音文件格式
                if v in [3, 4, 5, 6]:
                    self.options2[k] = v
                else:
                    self.options2[k] = 3
            else:
                pass  # 多余参数扔掉

    def run(self):
        result = self.client.synthesis(text=self.text, options=self.options2)
        return result


class Translate(object):
    url = "http://api.fanyi.baidu.com/api/trans/vip/translate"

    def __init__(self, auths, text, params={}):
        self.appid = auths["appid"]
        self.secretKey = auths["secretkey"]
        self.q = text
        self.fromlang = params.get("en", "en")
        self.tolang = params.get("zh", "zh")
        self.salt = str(int(time.time()))
        self.sign = ""
        self.params2 = {}

    def _get_sign(self):
        string = self.appid + self.q + self.salt + self.secretKey
        m = hashlib.md5()
        m.update(string.encode())
        self.sign = m.hexdigest()

    def _redo_params(self):
        self.params2 = {
                "appid": self.appid,
                "q": self.q,
                "from": self.fromlang,
                "to": self.tolang,
                "salt": self.salt,
                "sign": self.sign
                }

    def run(self):
        self._get_sign()
        self._redo_params()
        res = requests.get(self.url, params=self.params2)
        datas = json.loads(res.content)
        # {'from': 'en', 'to': 'zh', 'trans_result': [{'src': 'English', 'dst': '英语'}]}
        result = datas["trans_result"][0]["dst"]
        return result


if __name__ == '__main__':
    pass
