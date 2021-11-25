import tqdm
import time
import random

#插入排序
# 定义函数 insertion_sort 接受参数 list_sort，并返回插入排序结果。
def insertion_sort(list_sort):
    start=time.time()
    for i in tqdm.tqdm(range(len(list_sort)),desc='插入排序'):
        n = i
        while n > 0:
            if list_sort[n] < list_sort[n - 1]:
                list_sort[n], list_sort[n - 1] = list_sort[n - 1], list_sort[n]
                n -= 1
            else:
                break
    end=time.time()
    print("插入排序用时%.2f"%(end-start))

#选择排序
def selection_sort(list_sort):
    start = time.time()
    list=[]
    for i in tqdm.tqdm(range(len(list_sort)),desc='选择排序'):
        list.append(min(list_sort))
        list_sort.remove(min(list_sort))
    end = time.time()
    print("插入排序用时%.2f" % (end - start))

#快速排序
def quick_sort(list_sort):
    start = time.time()
    """quick_sort"""
    if len(list_sort) >= 2:
        mid = list_sort[len(list_sort)//2]
        left,right = [], []
        list_sort.remove(mid)
        for num in tqdm.tqdm(list_sort,desc='快速排序'):
            if num >= mid:
                right.append(num)
            else:
                left.append(num)
        end = time.time()
        print("快速排序用时%.2f" % (end - start))


#希尔排序
def shell_sort(lists):
    pass


dict={1:'选择排序',2:'插入排序',3:'快速排序',4:'希尔排序'}
sort=['',
    'selection_sort(copy.deepcopy(list))',
    'insertion_sort(copy.deepcopy(list))',
    'quick_sort(copy.deepcopy(list))',
    'shell_sort(copy.deepcopy(list))']

if __name__ == '__main__':
    list=[]
    for i in range(10000):
        list.append(random.randint(0, 1000))
    shell_sort(list)