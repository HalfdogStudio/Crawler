#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
"""
我觉得我会用node来做这些？
"""

# r = requests.post("http://job.alibaba.com/
# zhaopin/socialPositionList/doList.json",
# data={"pageSize": 10, "t" : "0.37100800256153467", "pageIndex": 200})

# 第一次请求会返回有关信息。POST/GET均可，pageSize被阿里限制为500

JOB_DICT = {}

def request_job_list(pageIndex, pageSize):
    #try:
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
    #except:
    #    print "fail to request"
    #    pass
