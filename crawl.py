import json
import re
import time
import requests
from urllib import parse


def get_abstract(keyword):
    sess = requests.Session()
    site = f'https://www.lagou.com/jobs/list_{parse.quote(keyword)}'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
        'Referer': site
    }
    sess.get(site, headers=headers)
    data = {
        'first': 'true',
        'pn': '1',
        'kd': keyword,
    }

    url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=true'
    abstract = []
    try:
        for i in range(0, 200):
            if i > 0:
                data['first'] = 'false'
                data['pn'] = str(i + 1)
            print(f'Crawling page {i+1}...')
            res = sess.post(url, headers=headers, data=data, timeout=3000)
            data = json.loads(res.text, encoding='utf-8')
            abstract += data['content']['positionResult']['result']
            time.sleep(10)
    except:
        pass
    return abstract


def get_info(abstract_lists, filename):
    sess = requests.Session()
    f = open(filename, 'w', encoding='utf-8')
    headers = {
        'Content-Type':
        'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
    }
    for pos in abstract_lists:
        positionId = str(pos['positionId']).replace(' ', '')
        positionName = str(pos['positionName']).replace(' ', '')
        createTime = str(pos['createTime']).replace(' ', '')
        companyId = str(pos['companyId']).replace(' ', '')
        companyShortName = str(pos['companyShortName']).replace(' ', '')
        workYear = str(pos['workYear']).replace(' ', '')
        education = str(pos['education']).replace(' ', '')
        city = str(pos['city']).replace(' ', '')
        salary = str(pos['salary']).replace(' ', '')
        positionAdvantage = str(pos['positionAdvantage']).replace(' ', '')
        companySize = str(pos['companySize']).replace(' ', '')
        companyLabelList = str(pos['companyLabelList']).replace(' ', '')
        district = str(pos['district']).replace(' ', '')
        positionLables = str(pos['positionLables']).replace(' ', '')
        industryLables = str(pos['industryLables']).replace(' ', '')
        businessZones = str(pos['businessZones']).replace(' ', '')
        longitude = str(pos['longitude']).replace(' ', '')
        latitude = str(pos['latitude']).replace(' ', '')
        companyFullName = str(pos['companyFullName']).replace(' ', '')
        firstType = str(pos['firstType']).replace(' ', '')
        secondType = str(pos['secondType']).replace(' ', '')
        thirdType = str(pos['thirdType']).replace(' ', '')
        linestaion = str(pos['linestaion']).replace(' ', '')
        skillLables = str(pos['skillLables']).replace(' ', '')
        data_list = [
            positionId, positionName, createTime, companyId, companyShortName,
            workYear, education, city, salary, positionAdvantage, companySize,
            companyLabelList, district, positionLables, industryLables,
            businessZones, longitude, latitude, companyFullName, firstType,
            secondType, thirdType, linestaion, skillLables
        ]
        site = f'https://www.lagou.com/jobs/{positionId}.html'
        res = sess.get(site, headers=headers, timeout=5000)
        f.write(' '.join(data_list) + ' ')
        # 直接存起来，需要用到的时候再提取信息处理
        f.write(
            res.text.replace(' ', '').replace('\r\n', '').replace('\n', ''))
        f.write('\n')
        time.sleep(10)
    f.close()


if __name__ == "__main__":
    abstract = get_abstract('数据')
    get_info(abstract, 'data/info.txt')
