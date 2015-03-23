#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
"""
事业部数量
"""


def stastic_department(JOB_DICT):
    """docstring for stastic_department"""
    dep_dict = {}
    with open('department.csv', 'wb') as f:
        for k, v in JOB_DICT.iteritems():
            if v['departmentName'] not in dep_dict:
                dep_dict[v['departmentName']] = 1
            else:
                dep_dict[v['departmentName']] += 1
    return dep_dict

def save_as_csv(dep_dict):
    """docstring for save_as_csv"""
    with open('department.csv', 'wb') as f:
        f.write('事业部' + ',' + '数量' + '\n')
        for k, v in dep_dict.iteritems():
            f.write(','.join([k, str(v)]).encode('utf-8') + '\n')


def relation(dep_dict):
    """docstring for relation"""
    entry_dict = {}
    with open("relation.dot", "wb") as f:
        f.write("digraph 阿里事业部{\n")
        for lk in dep_dict.keys():
            kl = lk.split('-')
            for i in range(len(kl) - 1):
                entry = "\"" + kl[i].encode('utf8') + "\" -> \"" + kl[i+1].encode('utf8') + "\";\n"
                if entry not in entry_dict:
                    entry_dict[entry] = ""
                    f.write(entry)
        f.write("}")
    cmd = "dot -Tpng -o 部门关系.png relation.dot"
    subprocess.call(cmd, shell=True)
    return entry_dict


