import tqdm
import time
import copy


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

