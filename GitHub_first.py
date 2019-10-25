# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 17:10:20 2019

@author: user
"""

import pandas as pd
import re
import os
def read_files(path=r'#This is a specific path'):
    '''
    遍历读取指定路径文件夹所在的所有文件
    '''
    files=os.listdir(path)
    s=[]
    for file in files:
        if not os.path.isdir(file):
            f = open(path+'/'+file)
            iter_f=iter(f)
            Str=''
            for line in iter_f:
                Str=Str+line
            s.append(Str)
    f.close()
    return s
#此函数参考https://blog.csdn.net/LZGS_4/article/details/50371030

def match_key_words():
    '''
    匹配目的字段，这里的目的字段是邮件地址
    '''
    List=[]
    text=read_files()
    for item in text:
        item=str(item)
        pattern=re.compile(r'https?://(www\.)?[-a-z0-9_.:]+/feature/[-a-z0-9_.:@&?=+,.!/~*%$]*')
        matches=pattern.finditer(item)
        for match in matches:
            List.append(match.group(0))
    return List
#此函数参考了Corey Schafer的视频教学
def construct_dict():
    '''
    构造一个生成DataFrame所需的字典
    '''
    List=match_key_words()
    d={'URL':[]}
    for item in List:
        d['URL'].append(item)
    return d

def construct_dataframe():
    '''
    生成一个DataFrame
    '''
    data=construct_dict()
    frame=pd.DataFrame(data)
    return frame

    
def construct_excel():
    '''
    生成excel表格
    '''
    frame=construct_dataframe()
    frame.to_excel("randomname.xlsx")
    print(frame)

construct_excel()
