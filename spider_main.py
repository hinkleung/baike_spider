# coding:utf8
# 调度程序
from baike_spider import html_downloader
from baike_spider import html_outputer
from baike_spider import html_parser
from baike_spider import url_manager

#思路先搭建好框架再补全代码

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()                         #创建url管理器
        self.downloader = html_downloader.HtmlDownloader()           #创建网页下载器
        self.parser = html_parser.HtmlParser()                       #创建网页解析器
        self.outputer = html_outputer.HtmlOutputer()                 #创建输出器

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)                             #url管理器的add_new_url(url)方法，添加一个url进管理器
        while self.urls.has_new_url():                              #url管理器的has_new_url()方法，判断是否有待爬url
            try:
                new_url = self.urls.get_new_url()                   #url管理器的get_new_url()方法，取出一个url
                print("craw %d : %s"%(count,new_url))
                html_cont = self.downloader.download(new_url)       #网页下载器的download(url)方法，把当前url的网页数据下载下来
                new_urls, new_data = self.parser.parse(new_url, html_cont)  #网页解析器的parse(new_url, html_cont)方法，把刚刚网页有用的数据解析出来
                                                                            #并且返回一个url列表和有用的数据
                self.urls.add_new_urls(new_urls)                    #url管理器的add_new_urls(urls)方法，添加一个url列表
                self.outputer.collect_data(new_data)                #输出器的collect_data(data)方法，把刚刚有用的并解析完的数据存进去

                if count==1000:
                    break
                count+=1
            except Exception as e:
                print(str(e)+'   '+'这里抓取失败')
        self.outputer.output_html()                                 #写入html文件


if __name__ == "__main__":
    root_url = "http://baike.baidu.com/item/Python"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
