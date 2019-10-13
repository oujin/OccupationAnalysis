# OccupationAnalysis

分析职位信息，从而为学生学业方向提供指导。

本项目仅用于学术学习，严禁用于任何形式的商业行为，作者拒绝承担由于商业行为产生的一切法律责任。


1. 首先使用crawl.py抓取数据。
```bash
$ python crawl.py
```

2. 然后提取信息，如这里提取薪酬和职业技能。
```bash
$ sh count.sh
$ sh salary.sh
```

3. 对职业技能进行词云统计。
```bash
$ python mycloud.py
```

4. 求出薪酬分布。
```bash
$ python distribute.py
```