#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
#http://talent.baidu.com/baidu/web/templet1000/index/corpwebPosition1000baidu!getPostListByConditionBaidu?pc.currentPage=2&pc.rowSize=10000&releaseTime=0&keyWord=&positionType=0&trademark=1&workPlaceCode=&positionName=&recruitType=12&brandCode=1&searchType=1&workPlaceNameV=&positionTypeV=0&keyWordV=
# 我擦嘞，弹性工作？

def request_job_list():
    r = requests.get("http://talent.baidu.com/baidu/web/templet1000/index/corpwebPosition1000baidu!getPostListByConditionBaidu?pc.currentPage=1&pc.rowSize=%s&releaseTime=0&keyWord=&positionType=0&trademark=1&workPlaceCode=&positionName=&recruitType=12&brandCode=1&searchType=1&workPlaceNameV=&positionTypeV=0&keyWordV=" % 10000)
