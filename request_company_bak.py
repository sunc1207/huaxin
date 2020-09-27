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
for index,row in pd_company.iterrows():
    company = row['co_num']
    v = ast.literal_eval(row['devID_set'])
    company_dict[company] = v
# print(company_dict)

data = './data/huaxin_company.log'
for k, v in company_dict.items():
    # print(k + ':' + v)
    for item in v:
        print('item:' + item)
        for i in range(1, 5):
            url = 'http://10.10.12.3/YZ180/api/getSystemHistory?devid=DATACOLLECTOR_192/ENERGY/YDWL/1.0/%s&pageNo=%d&pageSize=10000&sign=1&btime=1586793600&etime=1597680000&accesskey=wizcloud&time=1447756521&token=2063a5ec8e97c9468513cf31c5a0073cfe6b1005' % (item, i)
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
                file = './file/%s/YZ180_DATACOLLECTOR_192_ENERGY_YDWL_1.0_%s.csv' % (k, item)
                with open(file, 'a', encoding='utf-8') as file:
                    file.write(str(r.content.decode('utf-8')) + '\n')
                data_path = './data/huaxin.log'
                with open(data_path, 'a', encoding='utf-8') as data:
                    data.write(url + ',' + str(time_s) + ',' + str(time_cost) + ',' + str(
                        r.json()['meta']['total_count']) + ',' + str(i) + '\n')
                print(url)
                print("num:", i)

