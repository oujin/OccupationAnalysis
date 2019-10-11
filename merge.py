import json


maps = {}
with open('data/profile.txt', 'r', encoding='utf-8') as f:
    line = f.readline()
    while line:
        page = json.loads(line, encoding='utf-8')
        # extract
        result = page['content']['positionResult']['result']
        for res in result:
            positionId = str(res['positionId']).replace(' ', '')
            positionName = str(res['positionName']).replace(' ', '')
            createTime = str(res['createTime']).replace(' ', '')
            companyId = str(res['companyId']).replace(' ', '')
            companyShortName = str(res['companyShortName']).replace(' ', '')
            workYear = str(res['workYear']).replace(' ', '')
            education = str(res['education']).replace(' ', '')
            city = str(res['city']).replace(' ', '')
            salary = str(res['salary']).replace(' ', '')
            positionAdvantage = str(res['positionAdvantage']).replace(' ', '')
            companySize = str(res['companySize']).replace(' ', '')
            companyLabelList = str(res['companyLabelList']).replace(' ', '')
            district = str(res['district']).replace(' ', '')
            positionLables = str(res['positionLables']).replace(' ', '')
            industryLables = str(res['industryLables']).replace(' ', '')
            businessZones = str(res['businessZones']).replace(' ', '')
            longitude = str(res['longitude']).replace(' ', '')
            latitude = str(res['latitude']).replace(' ', '')
            companyFullName = str(res['companyFullName']).replace(' ', '')
            firstType = str(res['firstType']).replace(' ', '')
            secondType = str(res['secondType']).replace(' ', '')
            thirdType = str(res['thirdType']).replace(' ', '')
            linestaion = str(res['linestaion']).replace(' ', '')
            skillLables = str(res['skillLables']).replace(' ', '')
            data = [
                positionName, createTime, companyId, companyShortName, 
                workYear, education, city, salary, positionAdvantage, companySize,
                companyLabelList, district, positionLables, industryLables,
                businessZones, longitude, latitude, companyFullName, firstType,
                secondType, thirdType, linestaion, skillLables
            ]
            maps[positionId] = ' '.join(data)
        line = f.readline()


with open('data/all.txt', 'w', encoding='utf-8') as f:
    with open('data/position.txt', 'r', encoding='utf-8') as fp:
        line = fp.readline()
        while line:
            items = line.split(' ', 1)
            f.write(' '.join([items[0], maps[items[0]], items[1]]))
            line = fp.readline()
