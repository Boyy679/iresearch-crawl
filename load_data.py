import json
import requests
import time
from tqdm import tqdm

#由于1650-4045的url中有很多是空信息，无法用循环进行爬取，
# 未来需要写一个函数从最新的url request中读取最后一条信息的freport.xxx并依次循环遍历所有的url并读取其中的request url
def print_all_url(): #1652-4045  #循环打印出所有的request_url
    list_all=[]
    list_freport=['1741','1837','1933','2052','2124','2203','2279','2354','2426','2482','2540','2606',
                  '2661','2944','3011','3067','3142','3198','3253','3309','3366','3422','3475','3527',
                  '3579','3632','3685','3736','3790','3844','3897','3951','4000','4045']#50
    for i in tqdm(range(0,len(list_freport))):
        request_url_for='https://www.iresearch.com.cn/api/products/GetReportList?fee=0&date=&lastId=freport.'
        num_middle=list_freport[i]
        request_url_back='&pageSize='
        number_end=str(50)
        url= request_url_for+num_middle+request_url_back+number_end
        list_all.append(url)
    return list_all

def load_json_RemoveDuplicates(): #将所有request_url里面的每条信息的json格式读取出来并保存在一起
    list_all=print_all_url()
    ID_all=[]
    n=len(list_all)
    for i in tqdm(range(0,n)):
        request_url=list_all[i]
        Response = requests.get(request_url)
        url_text = Response.text
        json_text = json.loads(url_text)
        ID_each = json_text['List']
        ID_all=ID_all+ID_each
    #result = [i for n, i in enumerate(ID_all) if i not in ID_all[:n]]#去重
    return ID_all

#如果爬取1650-4045大概需要1-3min
if __name__ == '__main__':
    time_start = time.time() #开始计时
    ID_all=load_json_RemoveDuplicates()
    time_end = time.time()  # 结束计时
    file = open('all_json.txt', 'w')
    file.write(str(ID_all))
    file.close()
    time_c = time_end - time_start
    print('time cost: ', time_c, 's')
