# -- coding: utf-8 --
# from PyTest import max

# print max(1,2)

# import requests
# import re
# import time
# import hashlib

# def get_page(url):
#     print('GET %s' %url)
#     try:
#         response=requests.get(url)
#         if response.status_code == 200:
#             return response.content
#     except Exception:
#         pass

# def parse_index(res):
#     obj=re.compile('class="items.*?<a href="(.*?)"',re.S)
#     detail_urls=obj.findall(res.decode('gbk'))
#     for detail_url in detail_urls:
#         if not detail_url.startswith('http'):
#             detail_url='http://www.xiaohuar.com'+detail_url
#         yield detail_url

# def parse_detail(res):
#     obj=re.compile('id="media".*?src="(.*?)"',re.S)
#     res=obj.findall(res.decode('gbk'))
#     if len(res) > 0:
#         movie_url=res[0]
#         return movie_url


# def save(movie_url):
#     response=requests.get(movie_url,stream=False)
#     if response.status_code == 200:
#         m=hashlib.md5()
#         m.update(('%s%s.mp4' %(movie_url,time.time())).encode('utf-8'))
#         filename=m.hexdigest()
#         with open(r'./movies/%s.mp4' %filename,'wb') as f:
#             f.write(response.content)
#             f.flush()


# def main():
#     index_url='http://www.xiaohuar.com/list-3-{0}.html'
#     for i in range(5):
#         # print('*'*50,i)
#         #爬取主页面
#         print index_url.format(i,)
#         index_page=get_page(index_url.format(i,))
#         # #解析主页面,拿到视频所在的地址列表
#         detail_urls=parse_index(index_page)
#         # #循环爬取视频页
#         for detail_url in detail_urls:
#             #爬取视频页
#             detail_page=get_page(detail_url)
#             #拿到视频的url
#             movie_url=parse_detail(detail_page)
#             print ("url",movie_url)
#             if movie_url:
#                 #保存视频
#                 # save(movie_url)
#                 pass


# if __name__ == '__main__':
#     main()


# #并发爬取
# from concurrent.futures import ThreadPoolExecutor
# import queue
# import requests
# import re
# import time
# import hashlib
# from threading import current_thread

# p=ThreadPoolExecutor(50)

# def get_page(url):
#     print('%s GET %s' %(current_thread().getName(),url))
#     try:
#         response=requests.get(url)
#         if response.status_code == 200:
#             return response.content
#     except Exception as e:
#         print(e)

# def parse_index(res):
#     print('%s parse index ' %current_thread().getName())
#     res=res.result()
#     obj=re.compile('class="items.*?<a href="(.*?)"',re.S)
#     detail_urls=obj.findall(res.decode('gbk'))
#     for detail_url in detail_urls:
#         if not detail_url.startswith('http'):
#             detail_url='http://www.xiaohuar.com'+detail_url
#         p.submit(get_page,detail_url).add_done_callback(parse_detail)

# def parse_detail(res):
#     print('%s parse detail ' %current_thread().getName())
#     res=res.result()
#     obj=re.compile('id="media".*?src="(.*?)"',re.S)
#     res=obj.findall(res.decode('gbk'))
#     if len(res) > 0:
#         movie_url=res[0]
#         print('MOVIE_URL: ',movie_url)
#         with open('db.txt','a') as f:
#             f.write('%s\n' %movie_url)
#         # save(movie_url)
#         p.submit(save,movie_url)
#         print('%s下载任务已经提交' %movie_url)
# def save(movie_url):
#     print('%s SAVE: %s' %(current_thread().getName(),movie_url))
#     try:
#         response=requests.get(movie_url,stream=False)
#         if response.status_code == 200:
#             m=hashlib.md5()
#             m.update(('%s%s.mp4' %(movie_url,time.time())).encode('utf-8'))
#             filename=m.hexdigest()
#             with open(r'./movies/%s.mp4' %filename,'wb') as f:
#                 f.write(response.content)
#                 f.flush()
#     except Exception as e:
#         print(e)

# def main():
#     index_url='http://www.xiaohuar.com/list-3-{0}.html'
#     for i in range(5):
#         print "网址",index_url.format(i,)
#         # p.submit(get_page,index_url.format(i,)).add_done_callback(parse_index)


# if __name__ == '__main__':
#     main()

# i=100000000+40001
# frameNum=6
# o_id=i-100000000
# # 40001
# if o_id/10000 == 4:
#     frameNum=4
#     print('true========')
# print(frameNum)
# print(o_id)

# print(r'''111
# ...111
# ...222
# ...\n
# ...333''')

# import os

# def main():
#     classmate=['jack','wang']
#     print(classmate)
#     print(len(classmate))
#     classmate.append('ren')
#     print(classmate)
#     # print(classmate)
#     # print(classmate)
#     if 0:
#         print('xxxxxxxxxxxxx')

# if __name__ == "__main__":
#     main()
# -*- coding: utf-8 -*-

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
# print(L[0][0])
# 打印Python:
# print(L[1][1])
# 打印Lisa:
# print(L[-1][-1])

# r=range(101)
# for target_list in r:
    # print(target_list)
# print(r)
# print('xxx'+ str())

# sum = 0
# for x in range(101):
    # sum = sum + x
# print(sum)

# myList=[1,2,3,4,5]
# Mytuple=[1,2,3]

# Myset=set([1,2,3])
# # MySet=set(myList)
# print(Myset)
# one=(1, 2, 3)
# two=(1, [2, 3])
# MyDic = {'one':Mytuple,'two':one,'three':two}   #放入dic中
# print(MyDic)
# MyDic = (Mytuple,one,two)   #放入dic中
# print(MyDic)

# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('bad operand type')
#     if x >= 0:
#         return x
#     else:
#         return -x

# print(my_abs(-10))

# def myTest(a=1,b=2):
    # print('a======',a,'b=========',b)


# myTest(2,b=10)

# from collections import Iterable


# a=[1,2,3,4,5]

# print(a[0:5:2])

# for target_list in expression_list:
#     pass

# if isinstance(a,Iterable):
    # print('=============')

# new_a=enumerate(a)


