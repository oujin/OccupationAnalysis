import json
import requests
import re
import time


def get_info_by_line(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        line = f.readline()
        while line:
            yield line
            line = f.readline()


def get_id(lines):
    for line in lines:
        data = json.loads(line, encoding='utf-8')
        for idkey in data['content']['hrInfoMap']:
            yield idkey


def spider(job_id, save_file):
    f = open(save_file, 'w', encoding='utf-8')
    cnt = 0
    for i in job_id:
        sess = requests.Session()
        site = f'https://www.lagou.com/jobs/{i}.html'
        headers = {
            'Content-Type':
            'application/x-www-form-urlencoded; charset=UTF-8',
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
        }
        print(f'Crawled {cnt+1} pages...')
        cnt += 1
        res = sess.get(site, headers=headers, timeout=5000)
        f.write(i + ' ')
        f.write(res.text.replace(' ', '').replace('\r\n', '').replace('\n', ''))
        f.write('\n')
        time.sleep(10)
    f.close()


# lines = get_info_by_line('data/profile.txt')
# ids = get_id(lines)
# spider(ids, 'data/positions.txt')

lines = get_info_by_line('data/error.txt')
# f = open('data/right.txt', 'w', encoding='utf-8')
f1 = open('data/error1.txt', 'w', encoding='utf-8')
cnt = 0
for line in lines:
    
    sess = requests.Session()
    line = line.replace('\n', '')
    items = line.split()
    print(f'Dealing with {cnt+1} pages...')
    f1.write(items[0])
    f1.write(' ')
    site = f'https://www.lagou.com/jobs/{items[0]}.html'
    headers = {
        'Content-Type':
        'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
    }
    print('Crawling data...')
    res = sess.get(site, headers=headers, timeout=5000)
    if '<!DOCTYPEhtml>' not in res.text:
        res = sess.get(site, headers=headers, timeout=5000)
    f1.write(res.text.replace(' ', '').replace('\r\n', '').replace('\n', ''))
    f1.write('\n')
    time.sleep(5)
    cnt += 1
    sess.close()

f1.close()