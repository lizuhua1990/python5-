import requests
import re
import configparser
import urllib
import os


class Conf_Read():
    def Read_file(self,filepath,section,option):
        cf = configparser.ConfigParser()
        cf.read(filepath)
        url = cf.get(section,option)
        return url
X=Conf_Read().Read_file(r'object_win4000.conf','PATH2','url')#获取配置文件内的IP
# www.win4000妹子图片站点
# [PATH1]
# url=http://www.win4000.com/
#
# [PATH2]
# url=http://www.win4000.com/meitu.html


Data_urls = requests.get(X).text
Data_urls1 = re.compile('http://www.win4000.com/meinv+\d+.html')#
Data_urls2 = re.findall(Data_urls1,Data_urls)
Data_urls2 = list(set(Data_urls2))
cont1 = 0
cont2 = 0
for i in Data_urls2:
    Y = i.split('.')[2]
    News_Url = requests.get(i).text
    pattern = re.compile(r'http://www.win4000.com/meinv+\d+.html')#正则专门匹配图片的URL
    url1 = re.findall(pattern,News_Url)#从HTML内匹配数据
    zutu_1 = list(set(url1))

    for i in zutu_1:

        zutu_1_1 = requests.get(i).text
        # print(zutu_1_1)
        pattern_1 = re.compile(str(r'http://www.win4000.com/meinv+\d+_+\d+.html'))  # 正则专门匹配图片的URL
        url1_1_1 = re.findall(pattern_1, zutu_1_1)  # 从HTML内匹配数据
        zutu_1_1_1 = (list(set(url1_1_1)))
        cont2+=1
        filename1 = os.mkdir(r'F:\python爬小姐姐\小姐姐%s\\' % cont2)
        list1 = list(set([]))
        for i in zutu_1_1_1:
            # print(i)
            News_1 = requests.get(i).text
            AD = (News_1.split('"'))
            for i in AD:
                I = i.split('/')

                if 'pic1.win4000.com' in I:
                    V = (i.split('?'))[0]
                    print(V)
                    list1.append(V)
                    break
            cont1 += 1
            filename ='F:\python爬小姐姐\小姐姐%s\\爬虫小姐姐第一章%s'%(cont2,cont1) + '.jpg' #命名文件
            with open(filename, 'w') as file:#新建文件
                urllib.request.urlretrieve(V, filename)#下载文件i，并且重命名为filename每次循环+1
        print("已经完成下载:第%s组图" % cont2)
print('共有图片：%s 张'% cont1)#计算下载文件数量









