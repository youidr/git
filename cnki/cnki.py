#conding:utf-8
"""
服务器上不存在此用户
xlist = etree.HTML(res.text)
temp = xlist.xpath('//*[@class="boc-list"]/ul/li/a')
prog = re.compile(r'\d{4}\-\d{2}\-\d{2}')
y = x.xpath('div/h1/text()')[0]
dt = prog.findall(y)
"""
import requests
import time
from lxml import etree
import re

class Cnki():
    def __init__(self):
        self.r = requests.session()
        self.headers = {
            'Host':'kns.cnki.net',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3298.4 Safari/537.36'
        }

    def getbody(self,geturl,params):
        getres = self.r.get(geturl,headers=self.headers,params=params)
        return getres

    def SearchHandler(self):
        Searchurl = 'http://kns.cnki.net/kns/request/SearchHandler.ashx'
        searchtime = time.ctime(time.time())
        searchtime = searchtime[:10] + searchtime[19:] + searchtime[10:19] + ' GMT+0800 (中国标准时间)'
        params = {
            'action': '',
            'NaviCode': '*',
            'ua': '1.21',
            'PageName': 'ASP.brief_result_aspx',
            'DbPrefix': 'SCDB',
            'DbCatalog': '中国学术文献网络出版总库',
            'ConfigFile': 'SCDB.xml',
            'db_opt': 'CJFQ,CJRF,CDFD,CMFD,CPFD,IPFD,CCND,CCJD',
            'his': '0',
            '__': searchtime
        }
        search_result = self.getbody(Searchurl,params)
        return search_result


def Send_mail():
    pass


def Get_datas(v):
    htmldata = etree.HTML(v)
    temp = htmldata.xpath('//*[@class="GridTableContent"]/tr')
    cnkiurl = 'http://kns.cnki.net'
    cnkidownurl = 'http://kns.cnki.net/kns/'
    for i in temp[1:]:
        title_name = i.xpath('td[2]/a/text()')[0].strip()
        print(title_name)
        title_link = cnkiurl + i.xpath('td[2]/a/@href')[0].strip()
        print(title_link)
        author_list = i.xpath('td[3]/a')
        author_lists = []
        for l in author_list:
            author_name = l.xpath('text()')[0].strip()
            author_link = cnkiurl + l.xpath('@href')[0].strip()
            author_lists.append((author_name, author_link))
        print(author_lists)
        source_name = i.xpath('td[4]/a/text()')[0].strip()
        print(source_name)
        source_link = cnkiurl + i.xpath('td[4]/a/@href')[0].strip()
        print(source_link)
        Publish_date = i.xpath('td[5]/text()')[0].strip()
        print(Publish_date)
        Sqls = i.xpath('td[6]/text()')[0].strip()
        print(Sqls)
        download_link = i.xpath('td[8]/a/@href')[0].strip().replace('../', cnkidownurl)
        print(download_link)
        read_link = cnkiurl + i.xpath('td[9]/a/@href')[0].strip()
        print(read_link)

C = Cnki()
params = {'dbprefix':'SCDB'}
queryurl = 'http://kns.cnki.net/kns/brief/brief.aspx'
C.getbody(queryurl,params)
print('等待3秒后执行')
time.sleep(3)
C.headers['Referer'] = 'http://kns.cnki.net/kns/brief/result.aspx?dbprefix=SCDB'
page  = 1
brief_params = {
    'curpage':str(page),
    'RecordsPerPage':'10',
    'QueryID':'0',
    'ID':'',
    'turnpage':'1',
    'tpagemode':'L',
    'dbPrefix':'SCDB',
    'Fields':'',
    'DisplayMode':'listmode',
    'PageName':'ASP.brief_result_aspx'
}
C.SearchHandler()
res = C.getbody(queryurl,brief_params)
prog = re.compile(r'找到(.*?)条结果')
datanums = prog.findall(res.text)
print(datanums)
#print(res.text)
Get_datas(res.text)
time.sleep(3)
if datanums:
    datanums = datanums[0].replace('&nbsp;','').replace(',','')
    print(datanums)
    datanums = int(datanums)
    if datanums % 50 == 0:
        pages = int(datanums / 50)
    else:
        pages = datanums // 50 + 1
    while page < pages:
        page += 1
        brief_params['curpage'] = str(page)
        res = C.getbody(queryurl, brief_params)
        if '服务器上不存在此用户' in res.text:
            C.SearchHandler()
            page -= 1
            Send_mail()
            continue
        Get_datas(res.text)






