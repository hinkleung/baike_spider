#coding:utf8

from urllib import request

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        response=request.urlopen(url)          #下载器的第一种方法，得到response

        if response.getcode()!=200:
            return None

        return response.read()