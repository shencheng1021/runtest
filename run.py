# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""
import unittest

import os
# import sys
# rootpath=str(r"C:\Users\DELL\PycharmProjects\pythonProject3")
# syspath=sys.path
# print(syspath)
# sys.path=[]
# sys.path.append(rootpath)#将工程根目录加入到python搜索路径中
# sys.path.extend([rootpath+i for i in os.listdir(rootpath) if i[0]!="."])#将工程目录下的一级目录添加到python搜索路径中
# sys.path.extend(syspath)


if __name__ == '__main__':

    dirname=os.path.dirname(__file__)+"/test_case"
    suite=unittest.defaultTestLoader.discover(dirname,pattern="test_login.py")
    unittest.main(defaultTest='suite',verbosity=0)