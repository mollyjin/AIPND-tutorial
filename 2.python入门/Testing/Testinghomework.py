#!/usr/bin/python
# -*- coding:utf-8 -*-

#1
#请倒叙打印 ['Beijing', 'Shanghai', 'Shenzhen', 'Guangzhou']
# list = ['Beijing', 'Shanghai', 'Shenzhen', 'Guangzhou']
# list.reverse()
# print(list)
#
# x=[3,1,6,5,19,2,4]
# y=[]
# i=0
# while(x[i]<10):
#     y.append(x[i])
#     print(y)
#     i +=1

# 请倒叙打印 ['Beijing', 'Shanghai', 'Shenzhen', 'Guangzhou']
#
# error =0，① while error：print“hello”②while (not 0): print "hello",两个代码块的执行结果分别是什么？为什么产生这种结果？
#
# x=[3,1,6,5,19,2,4], y=[], i=0, while(x[i]<10): y.append(x[i])      print(y), i +=1, y的最终输出结果是？
# 输出两个列表之间的不同元素，如:[1, 2, 3], [2, 3, 'a'] 则输出['a', 1]
# 如何利用range输出[1,2,3,4]?
#
# cities = ['Beijing', 'Shanghai', 'Shenzhen', 'Guangzhou']，请使用for语句遍历cities，输出cities中的元素。
# m = ['a','b','b','c','a','b','b','c'] dic = {} for item in m:    if item not in dic.keys():        ...   else:        ... 能不能只利用字典和循环，来数一下'a','b','c'在m中分别出现了几次？补上...的部分即可
#
# 请用代码计算 1+3+5…+99+101。
#
# 如何利用 range 输出:  -10, -40, -70
#
# all(range(6)) 会返回什么?
#
# x=0, if not x: print "True" else: print "False",该段代码的输出结果是？
#
# x=0，y=1, if x and y：print (“False”) elif x or y：print (“True”)，该段代码的输出结果是？
# 在python中如何实现3种及以上的条件判断?
#
# if（x>3）: print ("True") else: print ("False"),若x=2，则该段代码的执行结果是？
# 在循环中,pass, break, continue 的作用相同吗? 若不同,不同之处是什么?
#
# cities = ['Beijing', 'Shanghai', 'Shenzhen', 'Guangzhou']，city=[], for i in range(len(cities)): city.__________ ,请在空白处填写合适的代码，利用cities中的元素创建一个city列表。


L1 = [1,2,3,4,5]
L2 = ["star","moon"]
L3 = [1,2,"star"]
L =  [L1,L2,L3]

print(max(L,key=len))

m = ['a','b','b','c','a','b','b','c']
dic = {}
for item in m:
    if item not in dic.keys():
        dic[item] = 1
    else:
        dic[item] += 1
print(dic)


