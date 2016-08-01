import os
class Base:
    def __init__(self,folder):
        self.folder = folder
    def currentBase(self):
        _cur = self.folder
        return _cur
    def dPath(self):
        _path = os.path.join(self.currentBase(), 'database')
        return _path
    def storePath(self):
        os.chdir(self.dPath())
        _storepath = os.getcwd()
        return _storepath
    def checker(self):
        files = os.listdir(self.storePath())
        if files == []:
            return True
        else:
            return False






