# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests
import sys

class downloadNovel():
    def __init__(self):
        self.server = 'https://www.xbiquge.la'
        self.target = 'https://www.xbiquge.la/7/7928/'
        self.chapter_names = []
        self.chapter_urls = []
        self.chapter_nums = 0
        self.headers = {
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-368708839@10.108.160.18; JSESSIONID=aaaL2DMAbpTgg8Qpc2xUw; OUTFOX_SEARCH_USER_ID_NCOO=1451460344.418452; ___rl__test__cookies=1561684330987',
            'Referer': 'http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OSX10_14_2) AppleWebKit/537.36(KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }

    def get_download_url(self):
        # 获取下载链接
        html = requests.get(url=self.target, headers=self.headers).content.decode()
        bf = BeautifulSoup(html, features="html.parser")
        chapter_dom_list = bf.findAll('div', id='list')
        chapters = BeautifulSoup(str(chapter_dom_list[0])).find_all('a')
        self.chapter_nums = len(chapters)
        for chapter in chapters:
            self.chapter_names.append(chapter.string)
            self.chapter_urls.append(self.server + chapter.get('href'))

    def get_content(self, target):
        # 获取章节内容
        html = requests.get(url=target, headers=self.headers).content.decode()
        bf = BeautifulSoup(html, features="html.parser")
        texts = bf.findAll('div', id='content')
        return texts[0].text.replace('\xa0'*8,'\n\n')

    def write_to_file(self, name, path, text):
        # 写入文件存起来
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')

if __name__ == '__main__':
    d = downloadNovel()
    d.get_download_url()
    print('开始下载')
    for i in range(d.chapter_nums):
        d.write_to_file(d.chapter_names[i], '吞噬星空.txt', d.chapter_names[i])
        d.write_to_file(d.chapter_names[i], '吞噬星空.txt', d.get_content(d.chapter_urls[i]))
        sys.stdout.write("  已下载:%.3f%%" % float(i / d.chapter_nums) + '\r')
        sys.stdout.flush()
    print('下载完成')