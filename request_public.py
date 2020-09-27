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

pd_company = pd.read_csv('company_devID.csv')
company_dict = {}

for index, row in pd_company.iterrows():
    co_num = row['co_num']
    company = row['company']
    tup = (co_num,company)
    v = ast.literal_eval(row['devID_set'])
    company_dict[tup] = v

area_dict = {
    '188': 'HC041',
    '192': 'YZ180',
    '180': 'YZ188'
}

data = './data/huaxin_company.log'
for k, v in company_dict.items():
    # print(k[0])
    # print(k[1])
    company_num = k[0]
    company_name = k[1]
    area = k[0][0:3]
    area_map = area_dict[area]
    # print(area)
    for item in v:
        # print(item)
        for i in range(1, 5):
            url = 'http://10.10.12.3/%s/api/getSystemHistory?devid=DATACOLLECTOR_%s/ENERGY/YDWL/1.0/%s&pageNo=%d&pageSize=10000&sign=1&btime=1586793600&etime=1597680000&accesskey=wizcloud&time=1447756521&token=2063a5ec8e97c9468513cf31c5a0073cfe6b1005' % (area_map, area, item, i)
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
                mkpath = './file/%s' % company_num
                mkdir(mkpath)
                file = './file/%s/%s_DATACOLLECTOR_%s_ENERGY_1.0_%s.csv' % (company_num, area_map, area, company_num)
                with open(file, 'a', encoding='utf-8') as file:
                    for li in r.json()['data']:
                        row = str(li['Info']['Datetime'])+','+str(li['Info']['EP'])+','+str(li['Info']['EP_Sum'])+','+str(li['Info']['P_Min'])+','+str(li['Info']['P_Max'])+','+str(li['Info']['Id'])+','+company_name
                        file.write(row + '\n')
                data_path = './data/huaxin_company.log'
                with open(data_path, 'a', encoding='utf-8') as data:
                    data.write(url + ',' + str(time_s) + ',' + str(time_cost) + ',' + str(
                        r.json()['meta']['total_count']) + ',' + str(i) + '\n')
                print(url)
                print("num:", i)

