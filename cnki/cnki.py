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


C = Cnki()
params = {'dbprefix':'SCDB'}
queryurl = 'http://kns.cnki.net/kns/brief/brief.aspx'
C.getbody(queryurl,params)
print('等待3秒后执行')
time.sleep(3)
C.headers['Referer'] = 'http://kns.cnki.net/kns/brief/result.aspx?dbprefix=SCDB'
brief_params = {
    'curpage':'1',
    'RecordsPerPage':'50',
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
datanums = datanums[0].replace('&nbsp;','').replace(',','')
print(datanums)



