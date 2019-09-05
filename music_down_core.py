# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 15:35:07 2018

@author: root
"""

import requests,json
from bs4 import BeautifulSoup

down_url='http://musicapi.taihe.com/v1/restserver/ting?method=baidu.ting.song.playAAC&from=web&songid='

class musicDownCore:
    
    def __init__(self, song):
        self._song_ = song;
        status = self.get_down_info();
        if status == 'success':
            self.down_music_file();
        else:
            print("未找到相关信息");

    def get_down_info(self):
        
        reqJson = requests.get(down_url+self._song_.sid);
        reqJson.encoding = 'utf-8';
        file_url = ''
        show_url = ''
        respInfo = reqJson.json();
        if respInfo['error_code'] != 22000:
            return 'error';
        jsonData = json.loads(json.dumps(reqJson.json()));
        self._name_ = jsonData['songinfo']['title'];
        self._file_type_ = jsonData['bitrate']['file_extension'];
        self.filename = self._name_+'('+self._song_.author+').'+self._file_type_;
        print("已获取到音乐：",self.filename);
        try:
            file_url = jsonData['bitrate']['file_link'];
            self.file_down_url = file_url;
        except KeyError:
            show_url = jsonData['bitrate']['show_link'];
            self.file_down_url = show_url;
        self._get_down_data_();
        return 'success';
        print("获取音乐信息完毕")
        
    def _get_down_data_(self):
        reqData = requests.get(self.file_down_url);
        reqData.encoding = 'utf-8';
        self.data = reqData.content;
    def down_music_file(self):
        print("开始下载:", self.filename)
        with open(self.filename,'wb') as msc:
            msc.write(self.data);
        self._song_.is_down = 1;
        print("下载完毕")
            
    
if __name__ == '__main__':
    mdc = musicDownCore('266259728');
