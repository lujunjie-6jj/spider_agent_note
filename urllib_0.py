from urllib import request

if __name__ == '__main__':
    url='https://www.baidu.com/'
    with request.urlopen(url) as rsq:
        print('url:',rsq.geturl())
        print('info:',rsq.info())
        print('rsq类型:',type(rsq))

        r = rsq.read()
        print(type(r))

        html=r.decode()
        print(type(html))
        print('html:',html)
