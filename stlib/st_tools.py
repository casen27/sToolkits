# tools

class PicMixZip(object):
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
