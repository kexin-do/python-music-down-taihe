# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 14:55:45 2018

@author: root
"""

from urllib.parse import quote
from bs4 import BeautifulSoup
import requests,json
from music_down_object import musicDownObject
from music_down_core import musicDownCore
search_base_url='http://www.taihe.com/search/song'

class musicDownSearch:
    '''
        初始化方法 传入搜索关键字
    '''
    def __init__(self,key):
        self.key = key
        self.urlKey = quote(self.key,'utf-8')
        self.s = '1'
        self.jump = '0'
        self.start = '0'
        self.size = '20'
        self.thrid_type = '0'
        self.find_target="data-songitem='"
        self.find_target_end = "'"
        self.find_target_len = len(self.find_target)
        self.json_data_target = 'songItem'
        self.songList = [];
    
    def do_search(self):
        search_url = search_base_url+"?s="+self.s+"&key="+self.urlKey+"&jump="+self.jump+"&start="+self.start+"&size="+self.size+"&thrid_type="+self.thrid_type
        req = requests.get(search_url)
        req.encoding = "utf-8"
        
        html = BeautifulSoup(req.content,'html5lib');
        self.total = int(html.find_all('span',class_="number")[0].text);
        tmp = int(self.total/int(self.size));
        tmp = tmp if self.total%int(self.size) == 0 else tmp + 1
        self.pages = tmp if tmp < 50 else 50
        song_list = html.find_all('li',attrs={"data-songitem":True});
        for i in range(len(song_list)):
            self.songList.append(self._get_songitem_data_to_object(song_list[i],i));
        
    
    '''
        通过传入的li Tag 来获取歌曲的内容并组装到对象中
    '''
    def _get_songitem_data_to_object(self, song_li,index):
        song_str_li = str(song_li);
        len1 = song_str_li.index(self.find_target)+self.find_target_len;
        len2 = song_str_li[len1:].index(self.find_target_end);
        songItem_json_data = song_str_li[len1:len2+len1];
        songItem_json = json.loads(songItem_json_data);
        json_object = songItem_json[self.json_data_target];
        music = musicDownObject(json_object, index);
        return music;
       
if __name__ == "__main__":
    mds = musicDownSearch('安静')
    mds.do_search()
