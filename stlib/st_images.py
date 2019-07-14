# 图片工具处理的相关类


import os
import time

from PIL import Image, ImageDraw, ImageFont


class GIFSpliter(object):
    # gif分割器
    version = "1.0.3"

    def __init__(self, gif, workDir=None, format=None):
        self.gif = gif
        self.workDir = workDir
        self.rank = 1
        self.frames = 1
        self.base = ""
        self.ext = ""
        self.sep = "_"
        self.current_name = ""
        self.format = format if format in {".png", ".bmp", ".tif"} else ".png"

    def _get_basic(self):
        path, name = os.path.split(self.gif)
        self.base, self.ext = name.split(".")
        if self.workDir is None:  # 未指定目录，在gif原先的目录创建同基础名文件
            self.workDir = os.path.join(path, self.base)
        elif os.path.split(self.workDir)[1] == self.base:  # 指定的目录与gif基础名字一致
            pass
        else:  # 指定的目录与gif名字不一致，需要创建gif名字的文件夹
            self.workDir = os.path.join(self.workDir, self.base)
        if not os.path.isdir(self.workDir):
            os.makedirs(self.workDir)
        self.frames = self.image.n_frames
        self.rank = len(str(self.frames))

    def _get_current_name(self, num):
        n = str(num).rjust(self.rank, "0")
        name = self.base + self.sep + n + self.format
        self.current_name = os.path.join(self.workDir, name)
        # print(self.current_name)

    def run(self):
        try:  # 不是图片类的，混淆扩展名为图片类的其他文件
            self.image = Image.open(self.gif)
        except:
            return False

        try:  # 图片类，但不是gif
            self._get_basic()
        except:
            return False

        if self.image and self.frames:
            for pos in range(self.frames):
                self.image.seek(pos)
                self._get_current_name(pos + 1)
                self.image.save(self.current_name)
            return True
        else:
            return False


class GIFCombiner(object):
    # gif合成器
    version = "1.0.0"

    def __init__(self):
        pass

    """
    import imageio
    import os

    images = []
    filenames=sorted((fn for fn in os.listdir(".") if fn.endswith(".jpg"))) # 目录中带.png会bug
    print(filenames)
    for filename in filenames:
        print("添加：" + filename)
        images.append(imageio.imread(filename))
    imageio.mimsave("_gif.gif", images,duration=0.5)  # 0.5秒换页
    """


class GIFReverse(object):
    # gif倒序播放
    # 获取temp目录，解压为jpg，倒序，合成
    version = "1.0.0"

    def __init__(self):
        pass


class Image2CharArt(object):
    version = "1.0.1"
    ratio_limit_vip = 16384
    max_limit_vip = 16384
    ratio_limit = 5  # 图片自身wh比率限制
    max_limit = 640  # 最大输出的分辨率大边
    ascii = "@WM&QN%OBDmgGR8HbwA0Ud9$6KXZPhkoeaynuzxsv[]|{})(=<>+^!*~;_:,-`. "
    # 使用 CharArtString 按显示权重排序自定义字符串，建议使用64个字符
    ascii_len = len(ascii)
    ext = ".txt"

    def __init__(self, image, width=0, height=0, prop=True, output=None):
        self.width = width
        self.height = height
        self.prop = prop
        self.image = image
        self.output = self._get_output(output)

    def _vip_unlock(self):
        # 解锁vip，生成各种尺寸、比例的图片
        self.ratio_limit = self.ratio_limit_vip
        self.max_limit = self.max_limit_vip
        self.prop = False

    def _get_output(self, name):
        if isinstance(name, str):
            if not os.path.isfile(name):
                return name
        else:
            path = os.path.dirname(self.image)
            base = os.path.split(path)[1]
            name = base + "_" + str(int(time.time())) + self.ext
            return name

    def _check_params(self):
        if self.width and self.height:  # 输入带需求wh
            ratio = max(self.width, self.height) / min(self.width, self.height)
            if ratio > self.ratio_limit:
                return 1  # 用户需求wh比例不协调

        self.im = Image.open(self.image)
        w, h = self.im.size  # 图片实际大小
        max_side = max(w, h)
        min_side = min(w, h)
        ratio = max_side / min_side
        if ratio > self.ratio_limit:
            return 2  # 原始图片比例不协调

        if max_side < self.max_limit:  # 实际宽高都不超限
            if w == max_side:
                if not self.width:
                    self.width = w
                if self.prop:
                    self.height = int(h / w * self.width)
                else:
                    if not self.height:
                        self.height = h
            else:
                if not self.height:
                    self.height = h
                if self.prop:
                    self.width = int(w / h * self.height)
                else:
                    if not self.width:
                        self.width = w
        else:  # 有边长超限，忽略用户需求，限制最大长度，强制使用原长宽比
            if w == max_side:
                self.width = self.max_limit
                self.height = int(h / w * self.max_limit)
            else:
                self.height = self.max_limit
                self.width = int(w / h * self.max_limit)

        return 0  # 正常计算wh

    def _draw(self):
        im = self.im.resize((self.width, self.height))  # 必须重新指定

        def _get_char(r, g, b, alpha=256):
            if alpha == 0:
                return ' '
            gray = 0.2126 * r + 0.7152 * g + 0.0722 * b
            index = int(gray / 255 * self.ascii_len)
            return self.ascii[index]

        result = []
        for h in range(self.height):
            for w in range(self.width):
                char = _get_char(*im.getpixel((w, h)))
                result.append(char)
            result.append("\n")
        self.txt = "".join(result)

    def _save(self):
        with open(self.output, 'w') as fp:
            fp.write(self.txt)

    def run(self, vip=None):
        if vip == "vip":
            self._vip_unlock()
        checked = self._check_params()
        if checked:
            print("参数不符合要求！")
        else:
            self._draw()
            self._save()


class CharArtString(object):
    # 生成一组字符串，按显示权重重排序
    # 字符自身占面积越大，越趋向于黑色，
    # import string
    # char = string.printable
    # char_cleaned = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" + "!#$%&()*+,-./:;<=>?@[]^_`{|}~" + "'\"\\" + " "
    # 微软雅黑权重  """@WM&QN%OBDmgGR8HbpwA0Ud9$q6KXZPh4SV#EkC253oeaynYuFTzx7fsvL[]t|cj{}1?J)(/l\=rI<>+^i!*~";_:,-'`. """
    # 黑体权重      """MWNBQ$R8&DOGK#HSgU@0ACE%5P69mbdXwV3pq4Z2akeFh*oJyYsfcnuLT7[]|?xzt}{vj<>1)I(=!\+lr/i~"-^;_`:',. """
    # 楷体权重      """MWNBQ$R8&DOGK#HSgU@0ACE%5P69mbdXwV3pq4Z2akeFh*oJyYsfcnuLT7?[]|xzt}{vj<>1!)I(=\+lr/i~;"-^:,_`'. """
    # 微软雅黑    msyh.ttc
    # 黑体        simhei.ttf
    # 楷体        simkai.ttf
    version = "1.0.0"
    font = ImageFont.truetype("msyh.ttc", 128)

    def __init__(self, strings):
        self.strings = strings
        self.string2 = ""

    def _cou(self, index, char):
        im = Image.new("RGB", (256, 256), (0, 0, 0))
        draw = ImageDraw.Draw(im)
        draw.text((0, 0), char, fill=(255, 255, 255), font=self.font)
        # im.save("%d.bmp" % index,"bmp")
        w, h = im.size
        count = 0
        for i in range(h):
            for j in range(w):
                p = im.getpixel((j, i))
                if p != (0, 0, 0):
                    count += 1
        res = (index, count, char)
        print(res)
        return res

    def run(self):
        ascii = self.strings
        result = []
        for i, char in enumerate(ascii):
            res = self._cou(i, char)
            result.append(res)
        # print(result)

        result2 = sorted(result, key=lambda t: t[1], reverse=True)
        # print(result2)

        result3 = []
        for item in result2:
            result3.append(item[2])
        self.strings2 = "".join(result3)
        # print(strings2)
        return self.strings2


def test_image_char_art():
    w = h = 256
    pic = "test_image_char_art.bmp"
    im = Image.new("RGB", (w, h), (255, 255, 255))  # w*h 纯白
    for i in range(h):
        for j in range(w):
            im.putpixel((i, j), (j, j, j))
    im.save(pic)
    i2c = Image2CharArt(pic)
    i2c.run()
    print("Test_image_char_art_Done.")


if __name__ == "__main__":
    test_image_char_art()
