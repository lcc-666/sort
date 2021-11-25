import random
from test import *
import copy
dict[0]='退出'

num=input('请输入要排序的数字数量\n')
list=[]

for i in range(eval(num)):
    list.append(random.randint(0, 1000))

while True:
    print('请选择你要进行的操作'+str(dict)+'\n')
    process=input()
    if process=='0':
        print('感谢使用')
        break
    elif True:
        eval(sort[eval(process)])
    else:
        print('您输入的指令有误,请重新输入')