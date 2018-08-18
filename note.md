python 3.6

urlopen返回对象：

url='https://www.baidu.com/'
    with request.urlopen(url) as rsq:
    r = rsq.read()    
    html=r.decode()

chardet可以自动检测页面文件编码格式，但可能有误

