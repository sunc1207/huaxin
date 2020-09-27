import requests
import time

data = './data/huaxin.log'

for i in range(1,2):
    url = 'http://10.10.12.3/YZ180/api/getSystemHistory?devid=DATACOLLECTOR_192/ENERGY/YDWL/1.0/11&pageNo=%d&pageSize=150000&sign=1&btime=1491022009&etime=1491898409&accesskey=wizcloud&time=1447756521&token=2063a5ec8e97c9468513cf31c5a0073cfe6b1005'%(i)
    try:
        time_start = time.time()
        time_s = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        r = requests.get(url)
        r.raise_for_status()
    except requests.RequestException as e:
        time_end = time.time()
        time_cost = time_end - time_start
        print('Time cost = %fs' % (time_end - time_start))
        with open (data, 'a', encoding = 'utf-8') as data:
            data.write(url + ',' + str(time_s) + ',' + str(time_cost) + ',' + str(e) + ',' + str(i) + '\n')
        print(e)
        print("num:",i)
        break
    else:
        time_end = time.time()
        time_cost = time_end - time_start
        print('Time cost = %fs' % (time_end - time_start))
        print(r.json()['meta']['total_count'])
        file = './file/YZ180_DATACOLLECTOR_192_ENERGY_YDWL_1.0_11.csv'
        with open (file, 'a', encoding = 'utf-8') as file:
            file.write(str(r.content.decode('utf-8'))+ '\n')
        data_path = './data/huaxin.log'
        with open (data_path, 'a', encoding = 'utf-8') as data:
            data.write(url + ',' + str(time_s) + ',' + str(time_cost) + ',' + str(r.json()['meta']['total_count']) + ',' + str(i) + '\n')
        print(url)
        print("num:",i)
