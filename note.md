python 3.6

urlopen返回对象：

url='https://www.baidu.com/'
    with request.urlopen(url) as rsq:
    r = rsq.read()    
    html=r.decode()
    
#可以自动检测页面文件编码格式，但可能有误
    chardet


#代理服务器步骤proxy：
    #1.设置代理地址
    proxy={'http':'120.194.13.6:81'}
    #2.创建ProxyHandler
    proxy_handler=request.ProxyHandler(proxy)
    #3.创建opener
    opener=request.build_opener(proxy_handler)
    #4.安装opener
    request.install_opener(opener)

#cookie & session
    -cookie是发送给用户（http浏览器的）的一段信息,单个cookie不超过4k,浏览器单个站点最多保存20个
    -session是保存在服务器上的对应的另一半信息，记录用户信息
    
    1.直接把cookie复制下来手动添加到headers中
    2.http模块包含一些cookie的模块，通过他们我们可以自动使用cookie
        -CookieJar
            -管理存储cookie，向传出的http请求添加cookie
            -cookie存储在内存中，CookieJar实例回收后cookie消失
        -FileCookieJar(filename,delayload=None,policy=None):
            -使用文件管理cookie
            -filename是保存cookie的文件
        -MozillaCookieJar(filename,delayload=None,policy=None):
            -创建与mocilla浏览器cookie.tet兼容的FileCookieJar实例
        -LwpCookieJar(filename,delayload=None,policy=None):
            -创建与libwww-perl标准兼容的Set-Cookie3格式的FileCookieJar实例
        -关系：CookieJar -> FileCookieJar -> MozillaCookieJar & LwpCookieJar