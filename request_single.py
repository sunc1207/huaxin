import requests
import time

#url = 'http://10.10.12.3/YZ180/api/getSystemHistory?devid=DATACOLLECTOR_192/ENERGY/YDWL/1.0/11&pageNo=1&pageSize=10000&sign=1&btime=1491022009&etime=1491898409&accesskey=wizcloud&time=1447756521&token=2063a5ec8e97c9468513cf31c5a0073cfe6b1005'

#for num in range(1, 159):
#    for i in range(1,500):
#        url = 'http://10.10.12.3/YZ180/api/getSystemHistory?devid=DATACOLLECTOR_192/ENERGY/YDWL/1.0/%d&pageNo=%d&pageSize=10000&sign=1&btime=1491022009&etime=1491898409&accesskey=wizcloud&time=1447756521&token=2063a5ec8e97c9468513cf31c5a0073cfe6b1005'%(num,i)
#        try:
#            r = requests.get(url, timeout=3000)
#            r.raise_for_status()
#        except requests.RequestException as e:
#            print(e)
#            print("device:%d, num:%d"%(num,i))
#            break
#        else:
#            file = 'YZ180_DATACOLLECTOR_192_ENERGY_YDWL_1.0_%d.csv'%(num)
#            with open (file, 'a', encoding = 'utf-8') as file:
#                file.write(str(r.content,encoding='utf-8'))
#                print("device:%d, num:%d"%(num,i))


for i in range(1,500):
    url = 'http://10.10.12.3/YZ180/api/getSystemHistory?devid=DATACOLLECTOR_192/ENERGY/YDWL/1.0/11&pageNo=%d&pageSize=10000&sign=1&btime=1491022009&etime=1491898409&accesskey=wizcloud&time=1447756521&token=2063a5ec8e97c9468513cf31c5a0073cfe6b1005'%(i)
    try: 
        time_start = time.time()   
        r = requests.get(url)
        r.raise_for_status()
    except requests.RequestException as e:
        time_end = time.time()
        print('Time cost = %fs' % (time_end - time_start))
        print(e)
        print("num:",i)
        break
    else:
        time_end = time.time()
        print('Time cost = %fs' % (time_end - time_start))
        file = 'YZ180_DATACOLLECTOR_192_ENERGY_YDWL_1.0_11.csv'
        with open (file, 'a', encoding = 'utf-8') as file:
            file.write(str(r.content,encoding='utf-8'))
            print(url)
            print("num:",i)

