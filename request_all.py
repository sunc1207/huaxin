import requests
import time
import pandas as pd
import ast
import os

def mkdir(path):
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        print
        path + ' 创建成功'
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print
        path + ' 目录已存在'
        return False
all_dict = {
    "180":[235,266,265,319],
    "192":[381,403,431,455],
    "188":[691,695,687,679,683,676]
}

area_dict = {
    '188':'HC041',
    '192':'YZ180',
    '180':'YZ188'
}

data = './data/huaxin_all.log'
for k,v in all_dict.items():
    all_district = k
    area_map = area_dict[k]
    for item in v:
        for i in range(1, 5):
            url = 'http://10.10.12.3/%s/api/getSystemHistory?devid=DATACOLLECTOR_%s/ENERGY/YDWL/1.0/%s&pageNo=%d&pageSize=10000&sign=1&btime=1586793600&etime=1597680000&accesskey=wizcloud&time=1447756521&token=2063a5ec8e97c9468513cf31c5a0073cfe6b1005' % (area_map, k, item, i)
            try:
                time_start = time.time()
                time_s = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                r = requests.get(url)
                r.raise_for_status()
            except requests.RequestException as e:
                time_end = time.time()
                time_cost = time_end - time_start
                print('Time cost = %fs' % (time_end - time_start))
                with open(data, 'a', encoding='utf-8') as data:
                    data.write(url + ',' + str(time_s) + ',' + str(time_cost) + ',' + str(e) + ',' + str(i) + '\n')
                print(e)
                print("num:", i)
                break
            else:
                time_end = time.time()
                time_cost = time_end - time_start
                print('Time cost = %fs' % (time_end - time_start))
                print(r.json()['meta']['total_count'])
                mkpath = './file/%s' % k
                mkdir(mkpath)
                file = './file/%s/%s_DATACOLLECTOR_%s_ENERGY_YDWL_1.0.csv' % (k, area_map, k)
                with open(file, 'a', encoding='utf-8') as file:
                    for li in r.json()['data']:
                        row = str(li['Info']['Datetime'])+','+str(li['Info']['EP'])+','+str(li['Info']['EP_Sum'])+','+str(li['Info']['P_Min'])+','+str(li['Info']['P_Max'])+','+str(li['Info']['Id'])+','+ k
                        file.write(row + '\n')
                data_path = './data/huaxin_all.log'
                with open(data_path, 'a', encoding='utf-8') as data:
                    data.write(url + ',' + str(time_s) + ',' + str(time_cost) + ',' + str(
                        r.json()['meta']['total_count']) + ',' + str(i) + '\n')
                print(url)
                print("num:", i)
