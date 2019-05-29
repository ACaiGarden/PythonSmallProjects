# -*- coding: UTF-8 -*-
import requests
import json

class WeiboSpider():
    def __init__(self):
        self.userID = 'target ID'
        self.pics_save_path = 'your path'
        self.page = 2

        self.url = 'https://m.weibo.cn/api/container/getIndex?' \
              'containerid=' + self.userID + '_-_WEIBO_SECOND_PROFILE_WEIBO&' \
              'page_type=03&page='

        self.headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                        #Remember to refresh the Cookie
                        'Cookie': 'your cookie',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                                  '(KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
                        'Referer': 'https://m.weibo.cn'
                        }


    def get_json(self):
        for x in range(1,self.page):
            r = requests.get(self.url + str(x), headers = self.headers).content
            print(r)
            self.json = r.decode('utf-8')
            self.analyse_json()

    def save_pics(self, path, pic_url):
        f = open(path + pic_url[-35:-4] + '.jpg', "wb")
        f.write(self.get_pics(pic_url))
        f.close()

    def get_pics(self, pic_url):
        p = requests.get(pic_url, headers = self.headers, timeout = 2).content
        return p

    def analyse_json(self):
        js_re = json.loads(self.json)
        print(js_re)
        for x in range(0, 10):
            try:
                '''
                After analysed the json which is got from the url,
                I find the way to get the large pictures.
                The Way:
                object=>data=>cards=>[0-10]=>mblog=>pics=>[0-pic_num]=>large=>url
                '''
                mblog = js_re['data']['cards'][int(x)]['mblog']
                print(x)
                if 'pics' in mblog:
                    for y in range(0, 10):
                        try:
                            pic_url = mblog['pics'][int(y)]['large']['url']
                            print(pic_url)
                            self.save_pics(self.pics_save_path, pic_url)
                        except:
                            pass
            except:
                pass


S = WeiboSpider()
S.get_json()