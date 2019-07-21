"""
链接百度API
使用库  https://github.com/Baidu-AIP/python-sdk
安装源  pip install git+https://github.com/Baidu-AIP/python-sdk.git@master
"""

import hashlib
import json
import os
import time

import requests
from aip import AipSpeech


class BaiduConnect(object):
    # 链接测试网络状况、账号密码是否可用
    version = "1.0.0"

    @classmethod
    def connect(cls, auths):
        # test 虚假链接成功
        return True

    @classmethod
    def connect1(cls, auths):
        # 测试链接：语音转文字、文字转语音、图片OCR
        try:
            sy = BaiduSynthesis(auths, "百度")
            result = sy.run()
        except:
            result = {}
        if isinstance(result, dict):
            # 链接失败
            print("百度语音文字OCR链接失败")
            return False
        else:
            # 链接成功，声音的二进制文件
            print("百度语音文字OCR链接成功")
            return True

    @classmethod
    def connect2(cls, auths):
        # 测试链接：翻译
        try:
            t = BaiduTranslate(auths=auths, params={"text": "English", "_return": 0})
            result = t.run()
        except:
            result = ""
        if result == "英语":
            print("百度翻译链接成功")
            return True
        else:
            print("百度翻译链接失败")
            return False


class BaiduASR(object):
    # 声音文件转字符串
    version = "1.0.0"

    def __init__(self, work_dir, file, auths):
        self.work_dir = work_dir
        self.file = file
        self.auths = {}
        # self.auths["appId"] = auths["appid"]
        self.auths["appId"] = ""
        self.auths["apiKey"] = auths["apikey"]
        self.auths["secretKey"] = auths["secretkey"]
        self.client = AipSpeech(**self.auths)

    def run(self):
        with open(self.file, "rb") as fp:
            rb = fp.read()
        ext = os.path.splitext(self.file)[1].lstrip(".")
        datas = self.client.asr(rb, ext)
        if datas.get("err_msg") == "success.":
            res = datas.get("result", "")
            str0 = res[0]
        else:
            str0 = json.dumps(datas, ensure_ascii=False)
        return str0

    """
    BaiduSynthesis
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


class BaiduSynthesis(object):
    # 字符串合成语音文件
    version = "1.0.0"

    def __init__(self, auths, text, options={}):
        self.auths = {}
        # self.auths["appId"] = auths["appid"]
        self.auths["appId"] = ""
        self.auths["apiKey"] = auths["apikey"]
        self.auths["secretKey"] = auths["secretkey"]
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
                pass

    def run(self):
        try:
            result = self.client.synthesis(text=self.text, options=self.options2)
        except:
            result = {"error_code": "0", "error_msg": "未知错误，检测网络链接、Keys是否有效"}
        return result


class BaiduTranslate(object):
    # 翻译
    # 百度官方技术说明
    # http://api.fanyi.baidu.com/api/trans/product/apidoc
    version = "1.0.0"
    url = "http://api.fanyi.baidu.com/api/trans/vip/translate"  # 接口
    lang_support = {"zh", "en", "yue", "wyw", "jp", "kor", "fra", "spa", "ru", "cht"}  # 更多语言查看技术文档
    q = ""
    fromlang = "auto"
    tolang = "zh"
    sign = ""
    _return = 0  # 返回上一层方式，1返回json.dumps字符串，0返回json解析后的译文字符串
    params2 = {}

    def __init__(self, auths, params={}):
        self.appid = auths.get("appid", "")
        self.secretKey = auths.get("secretkey", "")
        self.params = params
        self.salt = str(int(time.time()))
        self._check_params()

    def _check_params(self):
        # params={"text": "原始文本", "from":"zh", "to":"en", "_return": 0}
        fromlang = self.params.get("from")
        if fromlang in self.lang_support:
            self.fromlang = fromlang
        tolang = self.params.get("to")
        if tolang in self.lang_support:
            self.tolang = tolang
        text = self.params.get("text")
        if isinstance(text, str):
            self.q = text
        else:
            self.q = ""
        _return = self.params.get("_return")
        if _return in {0, 1}:
            self._return = _return
        else:
            self._return = 0

    def _get_sign(self):
        string = self.appid + self.q + self.salt + self.secretKey
        m = hashlib.md5()
        m.update(string.encode())
        self.sign = m.hexdigest()

    def _pack_params(self):
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
        self._pack_params()
        try:
            res = requests.get(self.url, params=self.params2)
            datas = json.loads(res.content)
        except:
            # {'error_code': '52003', 'error_msg': 'UNAUTHORIZED USER'}
            datas = {"error_code": "0", "error_msg": "未知错误，检测网络链接、Keys是否有效"}

        # http_response = {"from": "en", "to": "zh", "trans_result": [{"src": "English", "dst": "英语"}]}
        if self._return == 0:
            try:
                trans_result = datas.get("trans_result", "")
                if isinstance(trans_result, list):
                    li = []
                    for res in trans_result:
                        li.append(res["dst"])
                    return "\n".join(li)
            except:
                pass
        return json.dumps(datas, ensure_ascii=False, indent=4)
