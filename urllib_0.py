from urllib import request,parse

if __name__ == '__main__':
    url='https://www.baidu.com/'
    wd=input('输入你的关键字：')
    qs={'wd':wd}
    #转化url编码
    qs=parse.urlencode(qs)
    fullurl=url+qs
    print(qs)
    print(fullurl)
    with request.urlopen(fullurl) as rsq:

        print('url:',rsq.geturl())
        print('info:',rsq.info())
        print('code:',rsq.getcode())    #状态码    200
        print('rsq类型:',type(rsq))

        r = rsq.read()
        print(type(r))

        html=r.decode()
        print(type(html))
        print('html:',html)

