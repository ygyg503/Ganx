import urllib
url = "http://www.hao123.com"
filename = "./test.html"
urllib.urlretrieve(url,filename)
#urllib.urlretrieve()第一个参数为url 第二个参数为文件路径和文件名
#它直接把制定网页存储到本地文件中

