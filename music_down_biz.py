# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 09:47:58 2018

@author: root
"""

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from music_down_view import Ui_MusicDownView,DownButtonDelegate
from music_down_search import musicDownSearch
from music_down_core import musicDownCore
import sys

class musicDownBiz:
    
    def __init__(self,musicDownSearchObject):
        self.mds = musicDownSearchObject
        self.datas = musicDownSearchObject.songList
        app = QApplication(sys.argv)
        mainWindow = QMainWindow()
        self.ui = Ui_MusicDownView()
        self.ui.setupUi(mainWindow)
        self.dataView = self.ui.dataTable
        self._init__table_view()
        self.bindEvent4PageButton()        
        mainWindow.show()
        sys.exit(app.exec_())
    
    def _init__table_view(self):
        self.init_table_data()
        self.dataView.horizontalHeader().setStretchLastSection(True)
        self.dataView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.dataView.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def init_table_data(self):
        self.dataModel = QStandardItemModel(20,4)
        self.dataModel.setHorizontalHeaderLabels(['歌曲名称','作者','状态','操作','sid'])
        for row in range(len(self.datas)):
            data = self.datas[row];
            self.dataModel.setItem(row, 0, QStandardItem(data.sname))
            self.dataModel.setItem(row, 1, QStandardItem(data.author))
            self.dataModel.setItem(row, 2, QStandardItem(data.is_down))
            self.dataView.setItemDelegateForColumn(3, DownButtonDelegate(self))
            self.dataModel.setItem(row, 4, QStandardItem(data.sid))
        self.dataView.setModel(self.dataModel)
        self.dataView.setColumnHidden(4,True);#设置隐藏第四列
    
    def clickedDownButton(self, index):
        musicDownCore(self.datas[index[0]])
    
    def bindEvent4PageButton(self):
        self.ui.button_start.clicked.connect(lambda:self.gotoPage('start'));
        self.ui.button_pre.clicked.connect(lambda:self.gotoPage('pre'));
        self.ui.button_1.clicked.connect(lambda:self.gotoPage('1'));
        self.ui.button_2.clicked.connect(lambda:self.gotoPage('2'));
        self.ui.button_3.clicked.connect(lambda:self.gotoPage('3'));
        self.ui.button_next.clicked.connect(lambda:self.gotoPage('next'));
        self.ui.button_end.clicked.connect(lambda:self.gotoPage('end'));
        
    def gotoPage(self, toPage=None):
        currentPage = int(self.mds.start)
        totalPage = self.mds.pages
        button_1_page = int(self.ui.button_1.text())
        button_2_page = int(self.ui.button_2.text())-1
        button_3_page = int(self.ui.button_3.text())
        status = 'normal'
        
        if toPage == 'start':
            currentPage = '0'
            status = 'init'
        elif toPage == 'pre' or toPage == '1':
            if currentPage != 0:
                currentPage = str(currentPage - 1)
            else:
                currentPage = '0'
                status = 'init'
        elif toPage == 'next' or toPage == '3':
            if totalPage != currentPage:
                currentPage = str(currentPage + 1)
            else:
                currentPage = str(totalPage - 1)
                status = 'end';
        elif toPage == 'end':
            currentPage = str(totalPage - 1)
        elif toPage == '2' :
            if currentPage != button_2_page:
                currentPage = str(button_2_page - 1)
            else:
                currentPage = str(button_2_page)
        print('当前页：',currentPage,'总页数', str(totalPage))
        self.ui.page_info.setText('当前'+str(int(currentPage)+1)+'页/共'+str(totalPage)+'页')
        self.ui.page_count.setText('每页显示20条')
        self.updateNumberButton(status)
        self.mds.start = currentPage
        self.mds.do_search()
    
    def updateNumberButton(self,status):
        currentPage = int(self.mds.start)+1;
        if status == 'init':
            self.ui.button_1.setText('1')
            self.ui.button_2.setText('2')
            self.ui.button_3.setText('3')
        elif status == 'end':
            self.ui.button_1.setText(str(currentPage-2))
            self.ui.button_2.setText(str(currentPage-1))
            self.ui.button_3.setText(str(currentPage))
        else:
            self.ui.button_1.setText(str(currentPage))
            self.ui.button_2.setText(str(currentPage + 1))
            self.ui.button_3.setText(str(currentPage + 2))
    
if __name__ == "__main__":
    
    mds = musicDownSearch('安静')
    mds.do_search()
    mdb = musicDownBiz(mds)
