# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     02day
   Description :
   Author :        Liangz
   Date：          2018/12/4
-------------------------------------------------
   Change Activity:
                   2018/12/4:
-------------------------------------------------
"""
__author__ = 'Liangz'


import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Ico(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('2Day')
        self.setWindowIcon(QIcon('favicon.ico'))
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ico()
    sys.exit(app.exec_())
