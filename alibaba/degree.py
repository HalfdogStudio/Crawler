#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
学历要求
"""


def save_degree_as_csv(JOB_DICT):
    """docstring for save_degree_as_csv"""
    with open('degree.csv', 'wb') as f:
        f.write('类型1' + ',' '类型2' + ',' + '学历' + '\n')
        for k, v in JOB_DICT.iteritems():
            f.write(','.join([v['firstCategory'].encode('utf8'), v['secondCategory'].encode('utf8'),v['degree'].encode('utf8')]) + '\n')
