# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     DateWithPyQt5-1
   Description :
   Author :        Liangz
   Date：          2018/11/30
-------------------------------------------------
   Change Activity:
                   2018/11/30:
-------------------------------------------------
"""
__author__ = 'Liangz'


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication


class SigSlot(QWidget):
    def __init__(self):
        QWidget.__init__(self)                     # 界面初始化
        self.setWindowTitle('第一个PyQt5')          # 窗口标题
        lcd = QLCDNumber(self)                     # 模拟LCD显示器
        slider = QSlider(Qt.Horizontal, self)      # 滑动条

        vbox = QVBoxLayout()       # VBox布局方式
        vbox.addWidget(lcd)        # LCD 液晶显示器
        vbox.addWidget(slider)     # 滑动条

        self.setLayout(vbox)

        slider.valueChanged.connect(lcd.display)   # 滑动条的值改变的同时在LCD显示出来
        self.resize(350, 250)                      # 界面大小


app = QApplication(sys.argv)
gb = SigSlot()
gb.show()
sys.exit(app.exec_())
