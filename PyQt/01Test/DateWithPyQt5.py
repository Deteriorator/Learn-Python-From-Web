# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     DateWithPyQt5
   Description :
   Author :        Liangz
   Date：          2018/11/29
-------------------------------------------------
   Change Activity:
                   2018/11/29:
-------------------------------------------------
"""
__author__ = 'Liangz'


import sys
from PyQt5.QtWidgets import QWidget, QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)  # 初始化应用
    w = QWidget()                 # 初始化界面
    w.show()                      # 显示界面
    w.setWindowTitle("Hello")     # 窗口标题
    sys.exit(app.exec_())         # 关闭应用
