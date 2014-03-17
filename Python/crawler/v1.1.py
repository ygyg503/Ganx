#-*-coding:utf-8
import urllib  
#导入python标准库给我们提供的urllib
url = "http://www.hao123.com" 
#这个是我们要抓取的网页地址，一定不要忘记有http://这个符号哦
tmp_file = open("/home/yg/Code/Python/tmp.html","w")
#打开文件，传过去的参数的是你路径连文件名一起
tmp_file.write(urllib.urlopen(url).read())
#urllib.urlopen()大家可以查文档，意思穿过去url,a file-like object is returned
tmp_file.close()
#上完厕所要冲水，打开文件要关闭
#然后用浏览器打开文件看看
