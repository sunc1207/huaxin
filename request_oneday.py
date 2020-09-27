import requests
import time

data = './data/huaxin_oneday.log'

for i in range(1,5):
    url = 'http://10.10.12.3/YZ180/api/getSystemHistory?devid=DATACOLLECTOR_180/ENERGY/YDWL/1.0/277&pageNo=%d&pageSize=10000&sign=1&btime=1586793600&etime=1597680000&accesskey=wizcloud&time=1447756521&token=2063a5ec8e97c9468513cf31c5a0073cfe6b1005'%(i)
    try:
        time_start = time.time()
        time_s = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        r = requests.get(url)
        r.raise_for_status()
    except requests.RequestException as e:
        time_end = time.time()
        time_cost = time_end - time_start
        print('Time cost = %fs' % (time_end - time_start))
        with open (data_path, 'a', encoding = 'utf-8') as data:
            data.write(url + ',' + str(time_s) + ',' + str(time_cost) + ',' + str(e) + ',' + str(i) + '\n')
        print(e)
        print("num:%d"%(i))
    else:
        time_end = time.time()
        time_cost = time_end - time_start
        print('Time cost = %fs' % (time_end - time_start))
        print(r.json()['meta']['total_count'])
        file = './result/YZ180_DATACOLLECTOR_180_ENERGY_YDWL_1.0_277.csv'
        with open (file, 'a', encoding = 'utf-8') as file:
            for item in r.json()['data']:
                file.write(item['Info']['Datetime'] + '\n')
        data_path = './data/huaxin_oneday.log'
        with open (data_path, 'a', encoding = 'utf-8') as data:
            data.write(url + ',' + str(time_s) + ',' + str(time_cost) + ',' + str(r.json()['msg']) + ',' + str(i) + '\n')
        print(url)
        print("num:%d"%(i))

