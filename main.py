import random
from test import *
import copy

dict={1:'选择排序',2:'插入排序',3:'快速排序','q':'退出'}
num=input('请输入要排序的数字数量\n')
list=[]
for i in range(eval(num)):
    list.append(random.randint(0, 1000))
while True:
    print('请选择你要进行的操作'+str(dict)+'\n')
    process=input()
    if process=='q':
        print('感谢使用')
        break
    if process=='1':
        selection_sort(copy.deepcopy(list))
    if process=='2':
        insertion_sort(copy.deepcopy(list))
    if process=='3':
        quick_sort(copy.deepcopy(list))