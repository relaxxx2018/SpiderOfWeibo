import requests
from fake_useragent import UserAgent
import urllib.request

class Spider:
        headers = {
            "User-Agent": 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36',
            'Referer': 'https://m.weibo.cn/',
                }
        response = requests.get(url, headers=headers)
        data_json = json.loads(response.text)
        return data_json

    def get_data(self, data_json):
        d1 = data_json['data']
        d2 = d1['cards']
        for i in range(1, len(d2)):
            pics = []
            text = ''.join(re.findall(r'[\u4e00-\u9fa5，。？！]*', d2[i]['mblog']['text']))
            screen_name = d2[i]['mblog']['user']['screen_name']
            scheme = d2[i]['scheme']
            urls.append(scheme)
            # ''.join将list转换为字符串安装''分割
            print('博主：' + screen_name)
            print('内容：' + text)
            print('链接：' + scheme)
            if 'pics' in d2[i]['mblog']:
                for j in range(len(d2[i]['mblog']['pics'])):
                    pic = d2[i]['mblog']['pics'][j]['large']['url']
                    pics.append(pic)
                    print('图片链接：' + pic)
                self.download_pic(pics, text)
            if 'page_info' in d2[i]['mblog']:
                if 'media_info' in d2[i]['mblog']['page_info']:
                    mov = d2[i]['mblog']['page_info']['media_info']['stream_url']
                    print('视频链接：' + mov)
        return urls


    def download_pic(self, pics, text):
        for i in pics:
            print(i)
        dir = os.path.abspath('.\img')
        fulldir = dir + "\\" + text[0:20]
        if not os.path.exists(fulldir):
            os.makedirs(fulldir)

        for url in pics:
            pic_dir = fulldir + '\\' + url[56:61] + url[-4:]
            pic_content = requests.get(url).content
            f = open(pic_dir, 'wb')
            f.write(pic_content)
            f.close()
    def page_detail(self, urls):
        pass



if __name__ == '__main__':
    weibo = Spider()
    urls = []
    for i in range(1, 10):
        weibo.get_data(weibo.url_request(i))

    # for j in range(len(urls)):
    #     print(j)


