from typing import AsyncContextManager
import requests
import pandas as pd
import io
import time
import os

# create data folder or not
file_path = os.getcwd()+'/data/'

try:
    if not os.path.exists(file_path):
        os.makedirs(file_path)
        print('create a folder: '+file_path)
    else:
        print('folder exist')
except:
    print('create folder error')

# start get data
main_path = 'https://bas.nccc.com.tw/nccc-nop/OpenAPI/'
group = ['sexconsumption', 'ageconsumption',
         'incomegroupsconsumption', 'jobsconsumption', 'educationconsumption']
regionCode = {'KLC': '基隆市', 'TPE': '臺北市', 'NTP': '新北市', 'TYC': '桃園市', 'HCC': '新竹市',
              'HCH': '新竹縣', 'MLH': '苗栗縣', 'TCC': '臺中市', 'CHH': '彰化縣', 'NTH': '南投縣',
              'YUH': '雲林縣', 'CYC': '嘉義市', 'CYH': '嘉義縣', 'TNC': '臺南市', 'KHC': '高雄市',
              'PTH': '屏東縣', 'TTH': '臺東縣', 'HLH': '花蓮縣', 'YIH': '宜蘭縣', 'PHH': '澎湖縣',
              'KMH': '金門縣', 'LCH': '連江縣', 'TWN': '臺灣', 'X1': '無縣市'}
industryCode = {'FD': '食品餐飲類', 'CT': '服飾類', 'LG': '住宿類', 'TR': '交通類', 'EE': '文教康樂類',
                'DP': '百貨類', 'X2': '無產業', 'OT': '其他類'}

for i in group:
    all_data = pd.DataFrame()
    for j in list(regionCode):
        for k in list(industryCode):
            path = main_path+i+'/'+j+'/'+k
            rq = requests.get(path)
            if rq.text == '':
                break
            data = pd.read_csv(io.StringIO(rq.text), encoding='python')
            data['地區'] = regionCode[j]
            data['產業別'] = industryCode[k]
            all_data = all_data.append(data, ignore_index=True)
            print(i, regionCode[j], industryCode[k], ':'+str(len(data)))
            time.sleep(1)
    all_data.to_csv(file_path+i+'.csv', index=True, header=True)
