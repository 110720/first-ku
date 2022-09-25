import requests
r=requests.get("https://img1.baidu.com/it/u=3879871647,1191678062&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500/favicon.ico")
#在.py文件目录下保存图片
with open('favicon.ico','wb')as f:
    f.write(r.content)