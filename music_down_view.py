# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'musicDown.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Ui_MusicDownView(object):
    def setupUi(self, MusicDownView):
        MusicDownView.setObjectName("MusicDownView")
        MusicDownView.resize(800, 600)
        self.mainWidget = QtWidgets.QWidget(MusicDownView)
        self.mainWidget.setObjectName("mainWidget")
        self.dataTable = QtWidgets.QTableView(self.mainWidget)
        self.dataTable.setGeometry(QtCore.QRect(0, 40, 801, 471))
        self.dataTable.setObjectName("dataTable")
        self.searchButton = QtWidgets.QPushButton(self.mainWidget)
        self.searchButton.setGeometry(QtCore.QRect(676, 4, 75, 31))
        self.searchButton.setObjectName("searchButton")
        self.footerWidget = QtWidgets.QWidget(self.mainWidget)
        self.footerWidget.setGeometry(QtCore.QRect(20, 515, 761, 41))
        self.footerWidget.setObjectName("footerWidget")
        self.page_count = QtWidgets.QLabel(self.footerWidget)
        self.page_count.setGeometry(QtCore.QRect(30, 10, 121, 21))
        self.page_count.setObjectName("page_count")
        self.page_info = QtWidgets.QLabel(self.footerWidget)
        self.page_info.setGeometry(QtCore.QRect(120, 10, 121, 21))
        self.page_info.setObjectName("page_info")
        self.button_start = QtWidgets.QPushButton(self.footerWidget)
        self.button_start.setGeometry(QtCore.QRect(280, 10, 75, 23))
        self.button_start.setObjectName("button_start")
        self.button_pre = QtWidgets.QPushButton(self.footerWidget)
        self.button_pre.setGeometry(QtCore.QRect(360, 10, 75, 23))
        self.button_pre.setObjectName("button_pre")
        self.button_1 = QtWidgets.QPushButton(self.footerWidget)
        self.button_1.setGeometry(QtCore.QRect(440, 10, 31, 23))
        self.button_1.setObjectName("button_1")
        self.button_2 = QtWidgets.QPushButton(self.footerWidget)
        self.button_2.setGeometry(QtCore.QRect(480, 10, 31, 23))
        self.button_2.setObjectName("button_2")
        self.button_3 = QtWidgets.QPushButton(self.footerWidget)
        self.button_3.setGeometry(QtCore.QRect(520, 10, 31, 23))
        self.button_3.setObjectName("button_3")
        self.button_next = QtWidgets.QPushButton(self.footerWidget)
        self.button_next.setGeometry(QtCore.QRect(560, 10, 75, 23))
        self.button_next.setObjectName("button_next")
        self.button_end = QtWidgets.QPushButton(self.footerWidget)
        self.button_end.setGeometry(QtCore.QRect(640, 10, 75, 23))
        self.button_end.setObjectName("button_end")
        self.searchKey = QtWidgets.QPlainTextEdit(self.mainWidget)
        self.searchKey.setGeometry(QtCore.QRect(50, 4, 621, 31))
        self.searchKey.setObjectName("searchKey")
        MusicDownView.setCentralWidget(self.mainWidget)
        self.menubar = QtWidgets.QMenuBar(MusicDownView)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MusicDownView.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MusicDownView)
        self.statusbar.setObjectName("statusbar")
        MusicDownView.setStatusBar(self.statusbar)

        self.retranslateUi(MusicDownView)
        QtCore.QMetaObject.connectSlotsByName(MusicDownView)

    def retranslateUi(self, MusicDownView):
        _translate = QtCore.QCoreApplication.translate
        MusicDownView.setWindowTitle(_translate("MusicDownView", "MainWindow"))
        self.searchButton.setText(_translate("MusicDownView", "搜    索"))
        self.button_start.setText(_translate("MusicDownView", "首页"))
        self.button_pre.setText(_translate("MusicDownView", "上一页"))
        self.button_1.setText(_translate("MusicDownView", "1"))
        self.button_2.setText(_translate("MusicDownView", "2"))
        self.button_3.setText(_translate("MusicDownView", "3"))
        self.button_next.setText(_translate("MusicDownView", "下一页"))
        self.button_end.setText(_translate("MusicDownView", "尾页"))
        self.page_info.setText(_translate("MusicDownView", "当前C页/共T页"))
        self.page_count.setText(_translate("MusicDownView", "每页显示N条"))


class DownButtonDelegate(QItemDelegate):
    def __init__(self, mdb):
        self.mdb = mdb;
        super(DownButtonDelegate, self).__init__(mdb.dataView)

    def paint(self, painter, option, index):
        if not self.parent().indexWidget(index):
            self.button_down = QPushButton(
                self.tr('下载'),
                self.parent(),
                clicked=lambda:self.mdb.clickedDownButton(self.sender().index)
            )
            self.button_down.index = [index.row(), index.column()]
            h_box_layout = QHBoxLayout()
            h_box_layout.addWidget(self.button_down)
            h_box_layout.setContentsMargins(0, 0, 0, 0)
            h_box_layout.setAlignment(Qt.AlignCenter)
            widget = QWidget()
            widget.setLayout(h_box_layout)
            self.parent().setIndexWidget(index, widget)
       
