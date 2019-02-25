# #!/usr/bin/python
# # -*- coding:utf-8 -*-
# from typing import List, Any
#
# import pandas as pd
# import re
# import os
# import numpy as np
# import pinyin
# import matplotlib.pyplot as plt
# #%matplotlib inline
#
# print("所有库导入成功！")
#
# dataset = pd.read_csv('/Users/mollykings/Downloads/AIPND/AIPND-cn-trial-master/wechat_friends.csv').fillna('').to_dict('records')
#
# sex = {
#     'male': 0,
#     'female': 0,
#     'unknown': 0
# }
# for item in range(len(dataset)):
#     if dataset[item].get("Sex") == 1:
#         sex["male"]=sex["male"]+1
#     elif dataset[item].get("Sex") == 2:
#         sex["female"] = sex["female"] + 1
#     elif dataset[item].get("Sex") == 0:
#         sex["unknown"] = sex["unknown"] + 1
#
# print(sex)
# print("我的好友中共有", sex['male'],"位男性、", sex['female'], "位女性，有", sex['unknown'], "位好友未填写。")
#
# province = []
#
# for item in range(len(dataset)):
#     province.append(dataset[item].get("Province"))
# while '' in province:
#      province.remove('')
#
# print(dataset[1].get("Signature"))
#
# from snownlp import SnowNLP
#
# text = "这个商品我非常喜欢，颜色很合我意！"
# sentiment = SnowNLP(text).sentiments
#
# print(sentiment)

sentiments =[1,2,3,0.5,0.4,0.1,0.11,0.52]
positive = None
neutral = None
negative = None
positive = 0
neutral = 0
negative = 0
for x in sentiments:
    if x > 0.66:
        positive = positive + 1
    elif x >= 0.33 and x <= 0.66:
        neutral = neutral + 1
    elif x<0.33:
        negative = negative + 1

print(positive)
print(neutral)
print(negative)

