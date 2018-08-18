from urllib import request

if __name__ == '__main__':
    url='https://www.baidu.com/'
    with request.urlopen(url) as rsq:
        r = rsq.read()
        print(type(r))

        html=r.decode()
        print(type(html))

        print(html)
