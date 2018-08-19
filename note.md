python 3.6
#网易云课堂部分笔记
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
      
      
Requests-献给人类
HTTP for Humans，更简洁更友好

继承了urllib的所有特征

底层使用的是urllib3

开源地址： https://github.com/requests/requests

中文文档： http://docs.python-requests.org/zh_CN/latest/index.html

安装： conda install requests

get请求

requests.get(url)
requests.request("get", url)
可以带有headers和parmas参数
案例v21
get返回内容

案例v22
post

rsp = requests.post(url, data=data)
参看案例23
date, headers要求dict类型
proxy
      proxies = {
      "http":"address of proxy",
      "https": "address of proxy"
      }
      
      rsp = requests.request("get", "http:xxxxxx", proxies=proxies)
代理有可能报错，如果使用人数多，考虑安全问题，可能会被强行关闭
用户验证

代理验证

  #可能需要使用HTTP basic Auth， 可以这样
  # 格式为  用户名:密码@代理地址：端口地址
  proxy = { "http": "china:123456@192.168.1.123：4444"}
  rsp = requests.get("http://baidu.com", proxies=proxy)
web客户端验证

如果遇到web客户端验证，需要添加auth=（用户名，密码）

  autu=("test1", "123456")#授权信息
  rsp = requests.get("http://www.baidu.com", auth=auth)
cookie

requests可以自动处理cookie信息

    rsp = requests.get("http://xxxxxxxxxxx")
    # 如果对方服务器给传送过来cookie信息，则可以通过反馈的cookie属性得到
    # 返回一个cookiejar实例
    cookiejar = rsp.cookies   
    
    
    #可以讲cookiejar转换成字典
    cookiedict = requests.utils.dict_from_cookiejar(cookiejar)         
session

跟服务器端session不是一个东东

模拟一次会话，从客户端浏览器链接服务器开始，到客户端浏览器断开

能让我们跨请求时保持某些参数，比如在同一个session实例发出的 所有请求之间保持cookie

  # 创建session对象，可以保持cookie值
  ss = requests.session()
  
  headers = {"User-Agetn":"xxxxxxxxxxxxxxxxxx"}
  
  data = {"name":"xxxxxxxxxxx"}
  
  # 此时，由创建的session管理请求，负责发出请求，
  ss.post("http://www.baidu.com", data=data, headers=headers)
  
  rsp = ss.get("xxxxxxxxxxxx")
https请求验证ssl证书

参数verify负责表示是否需要验证ssL证书，默认是True

如果不需要验证ssl证书，则设置成False表示关闭

  rsp = requests.get("https://www.baidu.com", verify=False)
  # 如果用verify=True访问12306，会报错，因为他证书有问题 
  
#正则常用方法：
    match: 从开始位置开始查找，一次匹配
    search：从任何位置查找，一次匹配， 案例v25
    findall： 全部匹配，返回列表, 案例v26
    finditer： 全部匹配，返回迭代器, 案例v26
    split： 分割字符串，返回列表
    sub：替换
    中文unicode范围主要在[u4e00-u9fa5]
    
    
Selenium + PhantomJS
Selenium: web自动化测试工具
自动加载页面
获取数据
截屏
安装： pip install selenium==2.48.0
官网： http://selenium-python.readthedocs.io/index.html
PhantomJS(幽灵)
基于Webkit 的无界面的浏览器
官网： http://phantomjs.org/download.html
Selenium 库有有一个WebDriver的API
WebDriver可以跟页面上的元素进行各种交互，用它可以来进行爬取