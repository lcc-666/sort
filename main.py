import time
from test import Sort,dict,sort

def main():
    dict[0]='退出'
    dict['+']='重新输入排序数量'
    num=input('请输入要排序的数字数量\n')
    if num.isdigit():
        alist=Sort(int(num))
    else:
        print('您输入的不是数字,请从新输入')
        main()

    while True:
        print('请选择你要进行的操作'+str(dict)+'\n')
        process=input()
        if process=='+':
            main()
        if process=='0':
            print('感谢使用')
            time.sleep(3)
            exit()
        elif process in ['1','2','3','4']:
            eval(sort[eval(process)])
            print('\n')
        else:
            print('您输入有误请从新输入')


if __name__ == '__main__':
    main()
