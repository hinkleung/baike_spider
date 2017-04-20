# coding:utf8
from  bs4 import BeautifulSoup
import re
import urllib.parse


class HtmlParser(object):

    def parse(self, page_url, html_cont):                                              #传入一个url和下载器下载的内容
        if page_url is None or html_cont is None:
            return
        # 第二个参数是解析器，放入python自带的html.parser
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')           #bs4对象创建
        new_urls = self.__get_new_urls(page_url, soup)
        new_date = self.__get_new_date(page_url, soup)                                  #dict对象
        return new_urls, new_date

    def __get_new_urls(self, page_url, soup):                                         #传入page_url和bs4对象
        new_urls = set()                                                               #从有用数据中取出新的url装在一个set中
        links = soup.find_all('a', href=re.compile(r'/item/'))                          #findall方法获取数据中的url,利用正则表达式
        for link in links:
            new_url = link['href']                                                      #匹配到后用属性href拿url出来
            new_full_url = urllib.parse.urljoin(page_url, new_url)                      #拼接成完整的url
            new_urls.add(new_full_url)
        return new_urls

    def __get_new_date(self, page_url, soup):
        res_data = {}                                                                   #dict对象存储数据

        res_data['url']=page_url

        # <dd class="lemmaWgt-lemmaTitle-title"> <h1>Python</h1>
        title_node = soup.find('dd',class_="lemmaWgt-lemmaTitle-title").find("h1")      #连接两个find
        res_data['title']=title_node.get_text()                                         #

        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node=soup.find('div',class_="lemma-summary")
        res_data['summary']=summary_node.get_text()
        return res_data