import tqdm
import time
import numpy as np
import copy


class Sort():
    def __init__(self,num):
        self.alist = []
        for i in range(num):
            self.alist.append(i)
            np.random.shuffle(self.alist)
        print('数组初始化成功')

    def insertion_sort(self):
        list_sort=copy.deepcopy(self.alist)
        start = time.time()
        for i in tqdm.tqdm(range(len(list_sort)), desc='插入排序'):
            n = i
            while n > 0:
                if list_sort[n] < list_sort[n - 1]:
                    list_sort[n], list_sort[n - 1] = list_sort[n - 1], list_sort[n]
                    n -= 1
                else:
                    break
        end = time.time()
        print("插入排序用时%.2f" % (end - start))
        #print(list_sort)

    def selection_sort(self):
        list_sort=copy.deepcopy(self.alist)
        start = time.time()
        list = []
        for i in tqdm.tqdm(range(len(list_sort)), desc='选择排序'):
            list.append(min(list_sort))
            list_sort.remove(min(list_sort))
        end = time.time()
        print("选择排序用时%.2f" % (end - start))
        #print(list)

    def quick_sort(self):
        list_sort=copy.deepcopy(self.alist)
        start = time.time()
        """quick_sort"""
        if len(list_sort) >= 2:
            mid = list_sort[len(list_sort) // 2]
            left, right = [], []
            list_sort.remove(mid)
            for num in tqdm.tqdm(list_sort,desc='快速排序'):
                if num >= mid:
                    right.append(num)
                else:
                    left.append(num)
            print( self.quick_sort_2(left) + [mid] + self.quick_sort_2(right))
        else:
            print (list_sort)
            pass

        end=time.time()

        print("快速排序用时%.2f" % (end - start))

    def quick_sort_2(self,data):
        if len(data) >= 2:
            mid = data[len(data) // 2]
            left, right = [], []
            data.remove(mid)
            for num in data:
                if num >= mid:
                    right.append(num)
                else:
                    left.append(num)
            return self.quick_sort_2(left) + [mid] + self.quick_sort_2(right)
        else:
            return data



    def shell_sort(self):
        list=copy.deepcopy(self.alist)
        n = len(list)
        test = n // 2
        ls = []
        while True:
            test //= 2
            ls.append(test)
            if not test >= 1:
                break
        count = 0
        start = time.time()
        for gap in tqdm.tqdm(ls, desc='希尔排序'):
            count = count + 1
            for j in range(gap, n):
                i = j
                while (i - gap) >= 0:
                    if list[i] < list[i - gap]:
                        list[i], list[i - gap] = list[i - gap], list[i]
                        i -= gap
                    else:
                        break
        end = time.time()
        #print(list)
        print("希尔排序用时%.2f" % (end - start))


    def print(self):
        print(self.alist)





#
# #插入排序
# # 定义函数 insertion_sort 接受参数 list_sort，并返回插入排序结果。
# def insertion_sort(list_sort):
#     start=time.time()
#     for i in tqdm.tqdm(range(len(list_sort)),desc='插入排序'):
#         n = i
#         while n > 0:
#             if list_sort[n] < list_sort[n - 1]:
#                 list_sort[n], list_sort[n - 1] = list_sort[n - 1], list_sort[n]
#                 n -= 1
#             else:
#                 break
#     end=time.time()
#     print("插入排序用时%.2f"%(end-start))
#
# #选择排序
# def selection_sort(list_sort):
#     start = time.time()
#     list=[]
#     for i in tqdm.tqdm(range(len(list_sort)),desc='选择排序'):
#         list.append(min(list_sort))
#         list_sort.remove(min(list_sort))
#     end = time.time()
#     print("插入排序用时%.2f" % (end - start))
#
# #快速排序
# def quick_sort(data):
#     start = time.time()
#     """quick_sort"""
#     if len(data) >= 2:
#         mid = data[len(data) // 2]
#         left, right = [], []
#         data.remove(mid)
#         for num in data:
#             if num >= mid:
#                 right.append(num)
#             else:
#                 left.append(num)
#         return quick_sort(left) + [mid] + quick_sort(right)
#     else:
#         return data
#         # end = time.time()
#         # print("快速排序用时%.2f" % (end - start))
#
#
# #希尔排序
# def shell_sort(list):
#     n = len(list)
#     test=n//2
#     ls=[]
#     while True:
#         test //= 2
#         ls.append(test)
#         if not test >= 1:
#             break
#     count=0
#     start = time.time()
#     for gap in tqdm.tqdm(ls,desc='希尔排序'):
#         count=count+1
#         for j in range(gap, n):
#             i = j
#             while (i - gap) >= 0:
#                 if list[i] < list[i - gap]:
#                     list[i], list[i - gap] = list[i - gap], list[i]
#                     i -= gap
#                 else:
#                     break
#     end = time.time()
#     print("希尔排序用时%.2f" % (end - start))
#
#
#
#
#
dict={1:'选择排序',2:'插入排序',3:'快速排序',4:'希尔排序'}
sort=['',
    'alist.selection_sort()',
    'alist.insertion_sort()',
    'alist.quick_sort()',
    'alist.shell_sort()']

if __name__ == '__main__':
    pass