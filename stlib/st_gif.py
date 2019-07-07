# gif处理的相关类

import os

from PIL import Image


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
        self.format = format if format in {".png",".bmp",".tif"} else ".png"

    def _get_basic(self):
        path, name = os.path.split(self.gif)
        self.base, self.ext = name.split(".")
        if self.workDir is None:  # 未指定目录，在gif原先的目录创建同基础名文件
            self.workDir = os.path.join(path, self.base)
        elif os.path.split(self.workDir)[1] == self.base:  # 指定的目录与gif基础名字一致
            pass
        else:  # 指定的目录与gif名字不一致，需要创建gif名字的文件夹
            self.workDir = os.path.join(self.workDir,self.base)
        if not os.path.isdir(self.workDir):
            os.makedirs(self.workDir)
        self.frames = self.image.n_frames
        self.rank = len(str(self.frames))

    def _get_current_name(self, num):
        n = str(num).rjust(self.rank,"0")
        name = self.base + self.sep + n + self.format
        self.current_name = os.path.join(self.workDir,name)
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
