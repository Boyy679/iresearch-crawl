import requests
import os
import ast
from tqdm import tqdm

#all the class
#媒体文娱 ClassId: 59  广告营销 ClassId: 89  游戏行业 ClassId: 90  视频媒体 ClassId: 91
#消费电商 ClassId: 69  电子商务 ClassId: 86  消费者洞察 ClassId: 87  旅游行业 ClassId: 88
#汽车行业 ClassId: 80  教育行业 ClassId: 63  企业服务 ClassId: 60  网络服务 ClassId: 84
#应用服务 ClassId: 85  人工智能 ClassId: 83  支付行业 ClassId: 82  物流行业 ClassId: 75
#金融行业 ClassId: 70  AI大数据 ClassId: 65  房产行业 ClassId: 68  医疗健康 ClassId: 62
#先进制造 ClassId: 61  新能源 ClassId: 77  区块链 ClassId: 76  其他 ClassId: 81;  other


def save_pdf(path,json_num):
     url = "%s=%d" % ("https://www.iresearch.cn/include/ajax/user_ajax.ashx?work=idown&rid", json_num['NewsId'])
     down_res = requests.get(url)
     title = json_num['sTitle'].replace('/', '')
     filename = '{} {}'.format(path, title)
     with open(filename, 'wb') as file:
         file.write(down_res.content)

#ID_all:包含所有list的list
def download_classify(ID_all):
    for i in tqdm(ID_all):
        json_num=i
        if i['ClassId'] == 59: #媒体文娱
            if i['UserId']== 2022:
                save_pdf(folder59_2022,json_num)
            elif i['UserId'] == 2021:
                save_pdf(folder59_2021,json_num)
            elif i['UserId'] == 2020:
                save_pdf(folder59_2020,json_num)
            elif i['UserId'] == 2019:
                save_pdf(folder59_2019,json_num)
            elif i['UserId'] == 2018:
                save_pdf(folder59_2018,json_num)
            elif i['UserId'] == 2017:
                save_pdf(folder59_2017,json_num)
            elif i['UserId'] == 2016:
                save_pdf(folder59_2016,json_num)
            elif i['UserId'] == 2015:
                save_pdf(folder59_2015,json_num)
            elif i['UserId'] == 2014:
                save_pdf(folder59_2014,json_num)
            elif i['UserId'] == 2013:
                save_pdf(folder59_2013,json_num)
            elif i['UserId'] == 2012:
                save_pdf(folder59_2012,json_num)
            else:
                save_pdf(folder59_other,json_num)
        elif i['ClassId'] == 89: #广告营销
            if i['UserId']== 2022:
                save_pdf(folder89_2022,json_num)
            elif i['UserId'] == 2021:
                save_pdf(folder89_2021,json_num)
            elif i['UserId'] == 2020:
                save_pdf(folder89_2020,json_num)
            elif i['UserId'] == 2019:
                save_pdf(folder89_2019,json_num)
            elif i['UserId'] == 2018:
                save_pdf(folder89_2018,json_num)
            elif i['UserId'] == 2017:
                save_pdf(folder89_2017,json_num)
            elif i['UserId'] == 2016:
                save_pdf(folder89_2016,json_num)
            elif i['UserId'] == 2015:
                save_pdf(folder89_2015,json_num)
            elif i['UserId'] == 2014:
                save_pdf(folder89_2014,json_num)
            elif i['UserId'] == 2013:
                save_pdf(folder89_2013,json_num)
            elif i['UserId'] == 2012:
                save_pdf(folder89_2012,json_num)
            else:
                save_pdf(folder89_other,json_num)

        elif i['ClassId'] == 90: #游戏行业
            if i['UserId']== 2022:
                save_pdf(folder90_2022,json_num)
            elif i['UserId'] == 2021:
                save_pdf(folder90_2021,json_num)
            elif i['UserId'] == 2020:
                save_pdf(folder90_2020,json_num)
            elif i['UserId'] == 2019:
                save_pdf(folder90_2019,json_num)
            elif i['UserId'] == 2018:
                save_pdf(folder90_2018,json_num)
            elif i['UserId'] == 2017:
                save_pdf(folder90_2017,json_num)
            elif i['UserId'] == 2016:
                save_pdf(folder90_2016,json_num)
            elif i['UserId'] == 2015:
                save_pdf(folder90_2015,json_num)
            elif i['UserId'] == 2014:
                save_pdf(folder90_2014,json_num)
            elif i['UserId'] == 2013:
                save_pdf(folder90_2013,json_num)
            elif i['UserId'] == 2012:
                save_pdf(folder90_2012,json_num)
            else:
                save_pdf(folder90_other,json_num)

        elif i['ClassId'] == 91: #视频媒体
            if i['UserId']== 2022:
                save_pdf(folder91_2022,json_num)
            elif i['UserId'] == 2021:
                save_pdf(folder91_2021,json_num)
            elif i['UserId'] == 2020:
                save_pdf(folder91_2020,json_num)
            elif i['UserId'] == 2019:
                save_pdf(folder91_2019,json_num)
            elif i['UserId'] == 2018:
                save_pdf(folder91_2018,json_num)
            elif i['UserId'] == 2017:
                save_pdf(folder91_2017,json_num)
            elif i['UserId'] == 2016:
                save_pdf(folder91_2016,json_num)
            elif i['UserId'] == 2015:
                save_pdf(folder91_2015,json_num)
            elif i['UserId'] == 2014:
                save_pdf(folder91_2014,json_num)
            elif i['UserId'] == 2013:
                save_pdf(folder91_2013,json_num)
            elif i['UserId'] == 2012:
                save_pdf(folder91_2012,json_num)
            else:
                save_pdf(folder91_other,json_num)

        elif i['ClassId'] == 69: #消费电商
            if i['UserId']== 2022:
                save_pdf(folder69_2022,json_num)
            elif i['UserId'] == 2021:
                save_pdf(folder69_2021,json_num)
            elif i['UserId'] == 2020:
                save_pdf(folder69_2020,json_num)
            elif i['UserId'] == 2019:
                save_pdf(folder69_2019,json_num)
            elif i['UserId'] == 2018:
                save_pdf(folder69_2018,json_num)
            elif i['UserId'] == 2017:
                save_pdf(folder69_2017,json_num)
            elif i['UserId'] == 2016:
                save_pdf(folder69_2016,json_num)
            elif i['UserId'] == 2015:
                save_pdf(folder69_2015,json_num)
            elif i['UserId'] == 2014:
                save_pdf(folder69_2014,json_num)
            elif i['UserId'] == 2013:
                save_pdf(folder69_2013,json_num)
            elif i['UserId'] == 2012:
                save_pdf(folder69_2012,json_num)
            else:
                save_pdf(folder69_other,json_num)

        elif i['ClassId'] == 86: #电子商务
            if i['UserId']== 2022:
                save_pdf(folder86_2022,json_num)
            elif i['UserId'] == 2021:
                save_pdf(folder86_2021,json_num)
            elif i['UserId'] == 2020:
                save_pdf(folder86_2020,json_num)
            elif i['UserId'] == 2019:
                save_pdf(folder86_2019,json_num)
            elif i['UserId'] == 2018:
                save_pdf(folder86_2018,json_num)
            elif i['UserId'] == 2017:
                save_pdf(folder86_2017,json_num)
            elif i['UserId'] == 2016:
                save_pdf(folder86_2016,json_num)
            elif i['UserId'] == 2015:
                save_pdf(folder86_2015,json_num)
            elif i['UserId'] == 2014:
                save_pdf(folder86_2014,json_num)
            elif i['UserId'] == 2013:
                save_pdf(folder86_2013,json_num)
            elif i['UserId'] == 2012:
                save_pdf(folder86_2012,json_num)
            else:
                save_pdf(folder86_other,json_num)

        elif i['ClassId'] == 87: #消费者洞察
            if i['UserId']== 2022:
                save_pdf(folder87_2022,json_num)
            elif i['UserId'] == 2021:
                save_pdf(folder87_2021,json_num)
            elif i['UserId'] == 2020:
                save_pdf(folder87_2020,json_num)
            elif i['UserId'] == 2019:
                save_pdf(folder87_2019,json_num)
            elif i['UserId'] == 2018:
                save_pdf(folder87_2018,json_num)
            elif i['UserId'] == 2017:
                save_pdf(folder87_2017,json_num)
            elif i['UserId'] == 2016:
                save_pdf(folder87_2016,json_num)
            elif i['UserId'] == 2015:
                save_pdf(folder87_2015,json_num)
            elif i['UserId'] == 2014:
                save_pdf(folder87_2014,json_num)
            elif i['UserId'] == 2013:
                save_pdf(folder87_2013,json_num)
            elif i['UserId'] == 2012:
                save_pdf(folder87_2012,json_num)
            else:
                save_pdf(folder87_other,json_num)

        elif i['ClassId'] == 88: #旅游行业
            if i['UserId']== 2022:
                save_pdf(folder88_2022,json_num)
            elif i['UserId'] == 2021:
                save_pdf(folder88_2021,json_num)
            elif i['UserId'] == 2020:
                save_pdf(folder88_2020,json_num)
            elif i['UserId'] == 2019:
                save_pdf(folder88_2019,json_num)
            elif i['UserId'] == 2018:
                save_pdf(folder88_2018,json_num)
            elif i['UserId'] == 2017:
                save_pdf(folder88_2017,json_num)
            elif i['UserId'] == 2016:
                save_pdf(folder88_2016,json_num)
            elif i['UserId'] == 2015:
                save_pdf(folder88_2015,json_num)
            elif i['UserId'] == 2014:
                save_pdf(folder88_2014,json_num)
            elif i['UserId'] == 2013:
                save_pdf(folder88_2013,json_num)
            elif i['UserId'] == 2012:
                save_pdf(folder88_2012,json_num)
            else:
                save_pdf(folder88_other,json_num)

        elif i['ClassId'] == 80: #汽车行业
            if i['UserId']== 2022:
                save_pdf(folder80_2022,json_num)
            elif i['UserId'] == 2021:
                save_pdf(folder80_2021,json_num)
            elif i['UserId'] == 2020:
                save_pdf(folder80_2020,json_num)
            elif i['UserId'] == 2019:
                save_pdf(folder80_2019,json_num)
            elif i['UserId'] == 2018:
                save_pdf(folder80_2018,json_num)
            elif i['UserId'] == 2017:
                save_pdf(folder80_2017,json_num)
            elif i['UserId'] == 2016:
                save_pdf(folder80_2016,json_num)
            elif i['UserId'] == 2015:
                save_pdf(folder80_2015,json_num)
            elif i['UserId'] == 2014:
                save_pdf(folder80_2014,json_num)
            elif i['UserId'] == 2013:
                save_pdf(folder80_2013,json_num)
            elif i['UserId'] == 2012:
                save_pdf(folder80_2012,json_num)
            else:
                save_pdf(folder80_other,json_num)

        elif i['ClassId'] == 63: #教育行业
            if i['UserId']== 2022:
                save_pdf(folder63_2022,json_num)
            elif i['UserId'] == 2021:
                save_pdf(folder63_2021,json_num)
            elif i['UserId'] == 2020:
                save_pdf(folder63_2020,json_num)
            elif i['UserId'] == 2019:
                save_pdf(folder63_2019,json_num)
            elif i['UserId'] == 2018:
                save_pdf(folder63_2018,json_num)
            elif i['UserId'] == 2017:
                save_pdf(folder63_2017,json_num)
            elif i['UserId'] == 2016:
                save_pdf(folder63_2016,json_num)
            elif i['UserId'] == 2015:
                save_pdf(folder63_2015,json_num)
            elif i['UserId'] == 2014:
                save_pdf(folder63_2014,json_num)
            elif i['UserId'] == 2013:
                save_pdf(folder63_2013,json_num)
            elif i['UserId'] == 2012:
                save_pdf(folder63_2012,json_num)
            else:
                save_pdf(folder63_other,json_num)

        elif i['ClassId'] == 60: #企业服务
            if i['UserId']== 2022:
                save_pdf(folder60_2022,json_num)
            elif i['UserId'] == 2021:
                save_pdf(folder60_2021,json_num)
            elif i['UserId'] == 2020:
                save_pdf(folder60_2020,json_num)
            elif i['UserId'] == 2019:
                save_pdf(folder60_2019,json_num)
            elif i['UserId'] == 2018:
                save_pdf(folder60_2018,json_num)
            elif i['UserId'] == 2017:
                save_pdf(folder60_2017,json_num)
            elif i['UserId'] == 2016:
                save_pdf(folder60_2016,json_num)
            elif i['UserId'] == 2015:
                save_pdf(folder60_2015,json_num)
            elif i['UserId'] == 2014:
                save_pdf(folder60_2014,json_num)
            elif i['UserId'] == 2013:
                save_pdf(folder60_2013,json_num)
            elif i['UserId'] == 2012:
                save_pdf(folder60_2012,json_num)
            else:
                save_pdf(folder60_other,json_num)

        elif i['ClassId'] == 84: #网络服务
            if i['UserId']== 2022:
                save_pdf(folder84_2022,json_num)
            elif i['UserId'] == 2021:
                save_pdf(folder84_2021,json_num)
            elif i['UserId'] == 2020:
                save_pdf(folder84_2020,json_num)
            elif i['UserId'] == 2019:
                save_pdf(folder84_2019,json_num)
            elif i['UserId'] == 2018:
                save_pdf(folder84_2018,json_num)
            elif i['UserId'] == 2017:
                save_pdf(folder84_2017,json_num)
            elif i['UserId'] == 2016:
                save_pdf(folder84_2016,json_num)
            elif i['UserId'] == 2015:
                save_pdf(folder84_2015,json_num)
            elif i['UserId'] == 2014:
                save_pdf(folder84_2014,json_num)
            elif i['UserId'] == 2013:
                save_pdf(folder84_2013,json_num)
            elif i['UserId'] == 2012:
                save_pdf(folder84_2012,json_num)
            else:
                save_pdf(folder84_other,json_num)

        elif i['ClassId'] == 85: #应用服务
            if i['UserId']== 2022:
                save_pdf(folder85_2022,json_num)
            elif i['UserId'] == 2021:
                save_pdf(folder85_2021,json_num)
            elif i['UserId'] == 2020:
                save_pdf(folder85_2020,json_num)
            elif i['UserId'] == 2019:
                save_pdf(folder85_2019,json_num)
            elif i['UserId'] == 2018:
                save_pdf(folder85_2018,json_num)
            elif i['UserId'] == 2017:
                save_pdf(folder85_2017,json_num)
            elif i['UserId'] == 2016:
                save_pdf(folder85_2016,json_num)
            elif i['UserId'] == 2015:
                save_pdf(folder85_2015,json_num)
            elif i['UserId'] == 2014:
                save_pdf(folder85_2014,json_num)
            elif i['UserId'] == 2013:
                save_pdf(folder85_2013,json_num)
            elif i['UserId'] == 2012:
                save_pdf(folder85_2012,json_num)
            else:
                save_pdf(folder85_other,json_num)

        elif i['ClassId'] == 65: #AI大数据
            if i['UserId']== 2022:
                save_pdf(folder65_2022,json_num)
            elif i['UserId'] == 2021:
                save_pdf(folder65_2021,json_num)
            elif i['UserId'] == 2020:
                save_pdf(folder65_2020,json_num)
            elif i['UserId'] == 2019:
                save_pdf(folder65_2019,json_num)
            elif i['UserId'] == 2018:
                save_pdf(folder65_2018,json_num)
            elif i['UserId'] == 2017:
                save_pdf(folder65_2017,json_num)
            elif i['UserId'] == 2016:
                save_pdf(folder65_2016,json_num)
            elif i['UserId'] == 2015:
                save_pdf(folder65_2015,json_num)
            elif i['UserId'] == 2014:
                save_pdf(folder65_2014,json_num)
            elif i['UserId'] == 2013:
                save_pdf(folder65_2013,json_num)
            elif i['UserId'] == 2012:
                save_pdf(folder65_2012,json_num)
            else:
                save_pdf(folder65_other,json_num)

        elif i['ClassId'] == 83: #人工智能
            if i['UserId']== 2022:
                save_pdf(folder83_2022,json_num)
            elif i['UserId'] == 2021:
                save_pdf(folder83_2021,json_num)
            elif i['UserId'] == 2020:
                save_pdf(folder83_2020,json_num)
            elif i['UserId'] == 2019:
                save_pdf(folder83_2019,json_num)
            elif i['UserId'] == 2018:
                save_pdf(folder83_2018,json_num)
            elif i['UserId'] == 2017:
                save_pdf(folder83_2017,json_num)
            elif i['UserId'] == 2016:
                save_pdf(folder83_2016,json_num)
            elif i['UserId'] == 2015:
                save_pdf(folder83_2015,json_num)
            elif i['UserId'] == 2014:
                save_pdf(folder83_2014,json_num)
            elif i['UserId'] == 2013:
                save_pdf(folder83_2013,json_num)
            elif i['UserId'] == 2012:
                save_pdf(folder83_2012,json_num)
            else:
                save_pdf(folder83_other,json_num)

        elif i['ClassId'] == 75: #物流行业
            if i['UserId']== 2022:
                save_pdf(folder75_2022,json_num)
            elif i['UserId'] == 2021:
                save_pdf(folder75_2021,json_num)
            elif i['UserId'] == 2020:
                save_pdf(folder75_2020,json_num)
            elif i['UserId'] == 2019:
                save_pdf(folder75_2019,json_num)
            elif i['UserId'] == 2018:
                save_pdf(folder75_2018,json_num)
            elif i['UserId'] == 2017:
                save_pdf(folder75_2017,json_num)
            elif i['UserId'] == 2016:
                save_pdf(folder75_2016,json_num)
            elif i['UserId'] == 2015:
                save_pdf(folder75_2015,json_num)
            elif i['UserId'] == 2014:
                save_pdf(folder75_2014,json_num)
            elif i['UserId'] == 2013:
                save_pdf(folder75_2013,json_num)
            elif i['UserId'] == 2012:
                save_pdf(folder75_2012,json_num)
            else:
                save_pdf(folder75_other,json_num)

        elif i['ClassId'] == 70: #金融行业
            if i['UserId']== 2022:
                save_pdf(folder70_2022,json_num)
            elif i['UserId'] == 2021:
                save_pdf(folder70_2021,json_num)
            elif i['UserId'] == 2020:
                save_pdf(folder70_2020,json_num)
            elif i['UserId'] == 2019:
                save_pdf(folder70_2019,json_num)
            elif i['UserId'] == 2018:
                save_pdf(folder70_2018,json_num)
            elif i['UserId'] == 2017:
                save_pdf(folder70_2017,json_num)
            elif i['UserId'] == 2016:
                save_pdf(folder70_2016,json_num)
            elif i['UserId'] == 2015:
                save_pdf(folder70_2015,json_num)
            elif i['UserId'] == 2014:
                save_pdf(folder70_2014,json_num)
            elif i['UserId'] == 2013:
                save_pdf(folder70_2013,json_num)
            elif i['UserId'] == 2012:
                save_pdf(folder70_2012,json_num)
            else:
                save_pdf(folder70_other,json_num)

        elif i['ClassId'] == 82: #支付行业
            if i['UserId']== 2022:
                save_pdf(folder82_2022,json_num)
            elif i['UserId'] == 2021:
                save_pdf(folder82_2021,json_num)
            elif i['UserId'] == 2020:
                save_pdf(folder82_2020,json_num)
            elif i['UserId'] == 2019:
                save_pdf(folder82_2019,json_num)
            elif i['UserId'] == 2018:
                save_pdf(folder82_2018,json_num)
            elif i['UserId'] == 2017:
                save_pdf(folder82_2017,json_num)
            elif i['UserId'] == 2016:
                save_pdf(folder82_2016,json_num)
            elif i['UserId'] == 2015:
                save_pdf(folder82_2015,json_num)
            elif i['UserId'] == 2014:
                save_pdf(folder82_2014,json_num)
            elif i['UserId'] == 2013:
                save_pdf(folder82_2013,json_num)
            elif i['UserId'] == 2012:
                save_pdf(folder82_2012,json_num)
            else:
                save_pdf(folder82_other,json_num)

        elif i['ClassId'] == 68: #房产行业
            if i['UserId']== 2022:
                save_pdf(folder68_2022,json_num)
            elif i['UserId'] == 2021:
                save_pdf(folder68_2021,json_num)
            elif i['UserId'] == 2020:
                save_pdf(folder68_2020,json_num)
            elif i['UserId'] == 2019:
                save_pdf(folder68_2019,json_num)
            elif i['UserId'] == 2018:
                save_pdf(folder68_2018,json_num)
            elif i['UserId'] == 2017:
                save_pdf(folder68_2017,json_num)
            elif i['UserId'] == 2016:
                save_pdf(folder68_2016,json_num)
            elif i['UserId'] == 2015:
                save_pdf(folder68_2015,json_num)
            elif i['UserId'] == 2014:
                save_pdf(folder68_2014,json_num)
            elif i['UserId'] == 2013:
                save_pdf(folder68_2013,json_num)
            elif i['UserId'] == 2012:
                save_pdf(folder68_2012,json_num)
            else:
                save_pdf(folder68_other,json_num)

        elif i['ClassId'] == 62: #医疗健康
            if i['UserId']== 2022:
                save_pdf(folder62_2022,json_num)
            elif i['UserId'] == 2021:
                save_pdf(folder62_2021,json_num)
            elif i['UserId'] == 2020:
                save_pdf(folder62_2020,json_num)
            elif i['UserId'] == 2019:
                save_pdf(folder62_2019,json_num)
            elif i['UserId'] == 2018:
                save_pdf(folder62_2018,json_num)
            elif i['UserId'] == 2017:
                save_pdf(folder62_2017,json_num)
            elif i['UserId'] == 2016:
                save_pdf(folder62_2016,json_num)
            elif i['UserId'] == 2015:
                save_pdf(folder62_2015,json_num)
            elif i['UserId'] == 2014:
                save_pdf(folder62_2014,json_num)
            elif i['UserId'] == 2013:
                save_pdf(folder62_2013,json_num)
            elif i['UserId'] == 2012:
                save_pdf(folder62_2012,json_num)
            else:
                save_pdf(folder62_other,json_num)

        elif i['ClassId'] == 61: #先进制造
            if i['UserId']== 2022:
                save_pdf(folder61_2022,json_num)
            elif i['UserId'] == 2021:
                save_pdf(folder61_2021,json_num)
            elif i['UserId'] == 2020:
                save_pdf(folder61_2020,json_num)
            elif i['UserId'] == 2019:
                save_pdf(folder61_2019,json_num)
            elif i['UserId'] == 2018:
                save_pdf(folder61_2018,json_num)
            elif i['UserId'] == 2017:
                save_pdf(folder61_2017,json_num)
            elif i['UserId'] == 2016:
                save_pdf(folder61_2016,json_num)
            elif i['UserId'] == 2015:
                save_pdf(folder61_2015,json_num)
            elif i['UserId'] == 2014:
                save_pdf(folder61_2014,json_num)
            elif i['UserId'] == 2013:
                save_pdf(folder61_2013,json_num)
            elif i['UserId'] == 2012:
                save_pdf(folder61_2012,json_num)
            else:
                save_pdf(folder61_other,json_num)

        elif i['ClassId'] == 77: #新能源
            if i['UserId']== 2022:
                save_pdf(folder77_2022,json_num)
            elif i['UserId'] == 2021:
                save_pdf(folder77_2021,json_num)
            elif i['UserId'] == 2020:
                save_pdf(folder77_2020,json_num)
            elif i['UserId'] == 2019:
                save_pdf(folder77_2019,json_num)
            elif i['UserId'] == 2018:
                save_pdf(folder77_2018,json_num)
            elif i['UserId'] == 2017:
                save_pdf(folder77_2017,json_num)
            elif i['UserId'] == 2016:
                save_pdf(folder77_2016,json_num)
            elif i['UserId'] == 2015:
                save_pdf(folder77_2015,json_num)
            elif i['UserId'] == 2014:
                save_pdf(folder77_2014,json_num)
            elif i['UserId'] == 2013:
                save_pdf(folder77_2013,json_num)
            elif i['UserId'] == 2012:
                save_pdf(folder77_2012,json_num)
            else:
                save_pdf(folder77_other,json_num)

        elif i['ClassId'] == 76: #区块链
            if i['UserId']== 2022:
                save_pdf(folder76_2022,json_num)
            elif i['UserId'] == 2021:
                save_pdf(folder76_2021,json_num)
            elif i['UserId'] == 2020:
                save_pdf(folder76_2020,json_num)
            elif i['UserId'] == 2019:
                save_pdf(folder76_2019,json_num)
            elif i['UserId'] == 2018:
                save_pdf(folder76_2018,json_num)
            elif i['UserId'] == 2017:
                save_pdf(folder76_2017,json_num)
            elif i['UserId'] == 2016:
                save_pdf(folder76_2016,json_num)
            elif i['UserId'] == 2015:
                save_pdf(folder76_2015,json_num)
            elif i['UserId'] == 2014:
                save_pdf(folder76_2014,json_num)
            elif i['UserId'] == 2013:
                save_pdf(folder76_2013,json_num)
            elif i['UserId'] == 2012:
                save_pdf(folder76_2012,json_num)
            else:
                save_pdf(folder76_other,json_num)

        elif i['ClassId'] == 81: #其他
            if i['UserId']== 2022:
                save_pdf(folder81_2022,json_num)
            elif i['UserId'] == 2021:
                save_pdf(folder81_2021,json_num)
            elif i['UserId'] == 2020:
                save_pdf(folder81_2020,json_num)
            elif i['UserId'] == 2019:
                save_pdf(folder81_2019,json_num)
            elif i['UserId'] == 2018:
                save_pdf(folder81_2018,json_num)
            elif i['UserId'] == 2017:
                save_pdf(folder81_2017,json_num)
            elif i['UserId'] == 2016:
                save_pdf(folder81_2016,json_num)
            elif i['UserId'] == 2015:
                save_pdf(folder81_2015,json_num)
            elif i['UserId'] == 2014:
                save_pdf(folder81_2014,json_num)
            elif i['UserId'] == 2013:
                save_pdf(folder81_2013,json_num)
            elif i['UserId'] == 2012:
                save_pdf(folder81_2012,json_num)
            else:
                save_pdf(folder81_other,json_num)

        else: #other
            if i['UserId']== 2022:
                save_pdf(folderother_2022,json_num)
            elif i['UserId'] == 2021:
                save_pdf(folderother_2021,json_num)
            elif i['UserId'] == 2020:
                save_pdf(folderother_2020,json_num)
            elif i['UserId'] == 2019:
                save_pdf(folderother_2019,json_num)
            elif i['UserId'] == 2018:
                save_pdf(folderother_2018,json_num)
            elif i['UserId'] == 2017:
                save_pdf(folderother_2017,json_num)
            elif i['UserId'] == 2016:
                save_pdf(folderother_2016,json_num)
            elif i['UserId'] == 2015:
                save_pdf(folderother_2015,json_num)
            elif i['UserId'] == 2014:
                save_pdf(folderother_2014,json_num)
            elif i['UserId'] == 2013:
                save_pdf(folderother_2013,json_num)
            elif i['UserId'] == 2012:
                save_pdf(folderother_2012,json_num)
            else:
                save_pdf(folderother_other,json_num)

if __name__ == '__main__':
    # 建立文件夹
    save_root_dir = '艾瑞咨询爬虫结果'
    os.makedirs(save_root_dir, exist_ok=True)
    cat = ['媒体文娱', '广告营销', '游戏行业', '视频媒体', '消费电商',
           '电子商务', '消费者洞察', '旅游行业', '汽车行业', '教育行业', '企业服务',
           '网络服务', '应用服务', 'AI大数据', '人工智能', '物流行业', '金融行业',
           '支付行业', '房产行业', '医疗健康', '先进制造', '新能源', '区块链', '其他', 'other']
    year = ['2022', '2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013',
            '2012', 'other']
    for i in cat:
        for j in year:
            dir = os.path.join(save_root_dir, i, j)
            os.makedirs(dir, exist_ok=True)

    # 创建路径信息
    createVar = locals()
    myVarList = []  # 存放自己创建的变量
    class_all = ['59', '89', '90', '91', '69', '86', '87', '88', '80', '63', '60', '84',
                 '85', '83', '82', '75', '70', '65', '68', '62', '61', '77', '76', '81', 'other']
    for i in range(12):
        for j in range(25):
            createVar['folder' + class_all[j] + '_' + year[i]] = '/home/jkyyai/PycharmProjects/iresearch/艾瑞咨询爬虫结果/' + cat[j] + '/' + year[i] + '/'
            myVarList.append(createVar['folder' + class_all[j] + '_' + year[i]])  # 变量就在列表里了

    f = open(r'all_json.txt', 'r')
    file_data = f.read()
    ID_all = ast.literal_eval(file_data)
    download_classify(ID_all)

