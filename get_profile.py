import requests
# from bs4 import BeautifulSoup
import re
import base64
from urllib import parse
import time
import json


def getInfo(keyword, filename):
    sess = requests.Session()
    site = f'https://www.lagou.com/jobs/list_{parse.quote(keyword)}'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
        'Referer': site
    }
    sess.get(site, headers=headers)
    data = {
        'first': 'true',
        'pn': '1',
        'kd': keyword,
        }
    
    url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=true'
    # f = open(filename, 'w+', encoding='utf-8')
    try:
        for i in range(0, 200):
            if i > 0:
                data['first'] = 'false'
                data['pn'] = str(i+1) 
            print(f'Crawling page {i+1}...')
            res = sess.post(url, headers=headers, data=data, timeout=3000)
            data = json.loads(res.text, encoding='utf-8')
            result = data['content']['positionResult']['result']
            time.sleep(10)
            yield result
            # for res in result:
            #     sess.get(site, headers=headers)
            #     positionId = str(res['positionId']).replace(' ', '')
            #     positionName = str(res['positionName']).replace(' ', '')
            #     createTime = str(res['createTime']).replace(' ', '')
            #     companyId = str(res['companyId']).replace(' ', '')
            #     companyShortName = str(res['companyShortName']).replace(' ', '')
            #     workYear = str(res['workYear']).replace(' ', '')
            #     education = str(res['education']).replace(' ', '')
            #     city = str(res['city']).replace(' ', '')
            #     salary = str(res['salary']).replace(' ', '')
            #     positionAdvantage = str(res['positionAdvantage']).replace(' ', '')
            #     companySize = str(res['companySize']).replace(' ', '')
            #     companyLabelList = str(res['companyLabelList']).replace(' ', '')
            #     district = str(res['district']).replace(' ', '')
            #     positionLables = str(res['positionLables']).replace(' ', '')
            #     industryLables = str(res['industryLables']).replace(' ', '')
            #     businessZones = str(res['businessZones']).replace(' ', '')
            #     longitude = str(res['longitude']).replace(' ', '')
            #     latitude = str(res['latitude']).replace(' ', '')
            #     companyFullName = str(res['companyFullName']).replace(' ', '')
            #     firstType = str(res['firstType']).replace(' ', '')
            #     secondType = str(res['secondType']).replace(' ', '')
            #     thirdType = str(res['thirdType']).replace(' ', '')
            #     linestaion = str(res['linestaion']).replace(' ', '')
            #     skillLables = str(res['skillLables']).replace(' ', '')
            #     data_list = [
            #         positionId, positionName, createTime, companyId, companyShortName, 
            #         workYear, education, city, salary, positionAdvantage, companySize,
            #         companyLabelList, district, positionLables, industryLables,
            #         businessZones, longitude, latitude, companyFullName, firstType,
            #         secondType, thirdType, linestaion, skillLables
            #     ]
            #     site = f'https://www.lagou.com/jobs/{positionId}.html'
            #     res = sess.get(site, headers=headers, timeout=5000)
            #     f.write(' '.join(data_list) + ' ')
            #     f.write(res.text.replace(' ', '').replace('\r\n', '').replace('\n', ''))
            #     f.write('\n')
            #     time.sleep(10)
    except:
        pass
    # f.close()


getInfo('数据', 'data/raw_1.txt')
