import random


dict={1:'选择排序',2:'插入排序','q':'退出'}


while True:
    num=input('请输入要排序的数字数量\n')
    list=[]
    for i in range(eval(num)):
        list.append(random.randint(0, 1000))
    process=input(str(dict))