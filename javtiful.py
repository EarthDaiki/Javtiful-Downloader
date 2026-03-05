import requests
import re
import json
import os
from bs4 import BeautifulSoup

from SegmentsDownload import Downloader

class javtiful:
    def __init__(self):
        self.downloader = Downloader()
        self.session = requests.Session()

    def __get_video_id(self, url):
        match = re.search(r"/video/(\d+)/", url)
        if match:
            video_id = match.group(1)
            return video_id
        
    def __get_token(self, url):
        res = self.session.get(url)
        soup = BeautifulSoup(res.text, 'html.parser')
        token = soup.find(id="token_full").get("data-csrf-token")
        return token
        
    def get_video_info(self, url):
        video_id = self.__get_video_id(url)
        token = self.__get_token(url)
        payload = {
            'video_id': video_id,
            'pid_c': "",
            'token': token
        }
        res = self.session.post('https://javtiful.com/ajax/get_cdn', data=payload)
        print(res.text)
        if res.status_code != 200:
            print(res.text)
            raise
        return res.json()
    
    def __get_video_url(self, info):
        url = info['playlists']
        return url
    
    def __get_video_title(self, url):
        res = self.session.get(url)
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')  # HTMLを解析
            title = soup.title.string  # <title> の内容を取得
            title = re.sub(r'[\/:*?"<>|]', '', title)
            return title
        return 'Unknown'

    def run(self, url, output_folder):
        title = self.__get_video_title(url)
        info = self.get_video_info(url)
        raw_url = self.__get_video_url(info)
        self.downloader.get_video([raw_url], output_folder, title)