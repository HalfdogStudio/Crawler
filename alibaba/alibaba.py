#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import pickle
import csv
"""
我觉得我会用node来做这些？
"""

# r = requests.post("http://job.alibaba.com/
# zhaopin/socialPositionList/doList.json",
# data={"pageSize": 10, "t" : "0.37100800256153467", "pageIndex": 200})

# 第一次请求会返回有关信息。POST/GET均可，pageSize被阿里限制为500

JOB_DICT = {}

def request_job_list(pageIndex, pageSize):
    try:
        r = requests.get("http://job.alibaba.com/zhaopin/socialPositionList/doList.json?pageSize=%s&pageIndex=%s" % (str(pageSize), str(pageIndex)))
        # 返回的总信息
        data_1 = json.loads(r.content)
        if data_1[u'isSuccess'] is not True:
            return -1
        # 关于请求到的列表信息
        request_info = data_1[u'returnValue']
        totalPage = request_info[u'totalPage']
        pageSize = request_info[u'pageSize']
        pageIndex = request_info[u'pageIndex']
        totalRecord = request_info[u'totalRecord']
        print "-" * 20
        print "totalPage: ", totalPage
        print "pageIndex: ", pageIndex
        print "pageSize: ", pageSize
        print "totalRecord: ", totalRecord
        # 职位信息列表
        jobs = request_info['datas']
        for job in jobs:
            JOB_DICT[job['id']] = job
        if pageIndex < totalPage:
            request_job_list(pageIndex + 1, pageSize)
        else:
            return
    except:
        print "fail to request"
        pass


def save_as_csv(JOB_DICT):
    """字典是没有顺序的，但也不是随机的
    只要保证单次运行时写入顺序和排序是固定的就行
    """
    with open('alibaba.csv', 'wb') as f:
        csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        keys = JOB_DICT.itervalues().next().keys()
        #keys.pop(keys.index(u'description'))
        #keys.pop(keys.index(u'requirement'))
        #keys = ['code', 'secondCategory', 'workExperience', 'workLocation', 'departmentName', 'departmentId', 'degree', 'name', 'firstCategory']
        f.write(','.join(keys) + '\n')
        for k, v in JOB_DICT.iteritems():
            csv_writer.writerow([unicode(v[x]).encode('utf-8').replace(',', '，').replace('\r', '').replace('\n', '') for x in keys])


def save_dict(JOB_DICT):
    """docstring for save_dict"""
    pickle.dump(JOB_DICT, open("alibaba.p", 'wb'))


def load_dict():
    """docstring for load_dict"""
    return pickle.load("alibaba.p")
