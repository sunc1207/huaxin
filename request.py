import requests
import time

data_path = './data/huaxin.log'

#url = 'http://10.10.12.3/YZ180/api/getSystemHistory?devid=DATACOLLECTOR_192/ENERGY/YDWL/1.0/11&pageNo=1&pageSize=10000&sign=1&btime=1491022009&etime=1491898409&accesskey=wizcloud&time=1447756521&token=2063a5ec8e97c9468513cf31c5a0073cfe6b1005'

for num in range(1, 159):
    count = 1
    flag = 0
    for i in range(1,100000):
        url = 'http://10.10.12.3/YZ180/api/getSystemHistory?devid=DATACOLLECTOR_192/ENERGY/YDWL/1.0/%d&pageNo=%d&pageSize=10000&sign=1&btime=1491022009&etime=1491898409&accesskey=wizcloud&time=1447756521&token=2063a5ec8e97c9468513cf31c5a0073cfe6b1005'%(num,count)
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
            flag = flag + 1
            print(e)
            print("device:%d, num:%d"%(num,i))
            if flag > 1:
                time.sleep(120)
                break
            else:
                time.sleep(60)
                continue
        else:
            time_end = time.time()
            time_cost = time_end - time_start
            print('Time cost = %fs' % (time_end - time_start))
            print(r.json()['meta']['total_count'])
            count = count + 1
            file = './file/YZ180_DATACOLLECTOR_192_ENERGY_YDWL_1.0_%d.csv'%(num)
            with open (file, 'a', encoding = 'utf-8') as file:
                file.write(str(r.content.decode('utf-8'))+ '\n')
            data_path = './data/huaxin.log'
            with open (data_path, 'a', encoding = 'utf-8') as data:
                data.write(url + ',' + str(time_s) + ',' + str(time_cost) + ',' + str(r.json()['meta']['total_count']) + ',' + str(i) + '\n')
            print(url)
            print("device:%d, num:%d"%(num,i))
            flag = 0


#for i in range(1, 500):
#    url = 'http://10.10.12.3/YZ180/api/getSystemHistory?devid=DATACOLLECTOR_192/ENERGY/YDWL/1.0/11&pageNo=%d&pageSize=10000&sign=1&btime=1491022009&etime=1491898409&accesskey=wizcloud&time=1447756521&token=2063a5ec8e97c9468513cf31c5a0073cfe6b1005'%(i)
#    try:    
#        r = requests.get(url, timeout=3000)
#        r.raise_for_status()
#    except requests.RequestException as e:
#        print(e)
#        print("num:",i)
#        break
#    else:
#        with open ('huaxin.csv', 'a', encoding = 'utf-8') as file:
#            file.write(str(r.content,encoding='utf-8'))
#            print("num:",i)

