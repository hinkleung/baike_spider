#coding:utf8
class UrlManager(object):
    def __init__(self):
        self.new_urls=set()               #储存待爬的url的集合
        self.old_urls=set()               #储存已爬的url的集合

    def add_new_url(self, url):         #如果当前url不在url管理器的两个集合中，就添加到待爬url集合
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):       #将接收到的urls列表逐个用add_new_url(self, url)方法加入到待爬集合中
        if urls is None or len(urls)==0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):              #判空
        return len(self.new_urls)!=0

    def get_new_url(self):              #取出一个url，也将它pop出来并且add到已爬url集合中
        new_url=self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url

