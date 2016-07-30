import requests
import re

class crawler(object):

    def get_images(self, url):
        '''
        crawling images
        '''
        image_url = url[:url.index('?')]
        image_url = image_url.replace('biz', 'biz_photos')
        r = requests.get(image_url)
        text = r.text
        res = ['https:' + m for m in re.findall('src="(.*?\.jpg)" width="226"', text)]
        return res
