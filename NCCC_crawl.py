from typing import AsyncContextManager
import requests
import pandas as pd
import io
import time
import os

os.path

aa = requests.get(
    'https://bas.nccc.com.tw/nccc-nop/OpenAPI/sexconsumption/KLC/FD')

bb = aa.text

type(bb)

data = pd.read_csv(io.StringIO(bb))

data.columns


industryCode = {'FD': '食品餐飲類', 'CT': '服飾類', 'LG': '住宿類',
                'TR': '交通類', 'EE': '文教康樂類', 'DP': '百貨類', 'X2': '無產業', 'OT': '其他類'}
regionCode = {'KLC': '基隆市', 'TPE': '臺北市', 'NTP': '新北市', 'TYC': '桃園市', 'HCC': '新竹市', 'HCH': '新竹縣', 'MLH': '苗栗縣', 'TCC': '臺中市', 'CHH': '彰化縣', 'NTH': '南投縣', 'YUH': '雲林縣',
              'CYC': '嘉義市', 'CYH': '嘉義縣', 'TNC': '臺南市', 'KHC': '高雄市', 'PTH': '屏東縣', 'TTH': '臺東縣', 'HLH': '花蓮縣', 'YIH': '宜蘭縣', 'PHH': '澎湖縣', 'KMH': '金門縣', 'LCH': '連江縣', 'TWN': '臺灣', 'X1': '無縣市'}
industryCode
regionCode

group = ['sexconsumption', 'ageconsumption', 'incomeconsumption',
         'jobsconsumption', 'educationconsumption']
type(group)


for i in regionCode:
    print(i)
    print(regionCode[i])
