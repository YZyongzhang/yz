import urllib.request as url
request = url.Request(url='https://jwxt.bistu.edu.cn/jwapp/sys/wdkb/*default/index.do?EMAP_LANG=zh#/xskcb')
schedule_html = url.urlopen(request)
print(schedule_html)