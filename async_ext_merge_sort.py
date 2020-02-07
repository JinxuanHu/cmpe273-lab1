import asyncio
import numpy as np
import datetime

def OpenAndRead(filename):
    data_list = []
    with open(filename) as f:
        for line in f:
            data_list.append(int(line.rstrip('\n')))
    return data_list

matrix = []
merge_list = []

async def getMatrix():
    filenames = [
        "input/unsorted_1.txt",
        "input/unsorted_2.txt",
        "input/unsorted_3.txt",
        "input/unsorted_4.txt",
        "input/unsorted_5.txt",
        "input/unsorted_6.txt",
        "input/unsorted_7.txt",
        "input/unsorted_8.txt",
        "input/unsorted_9.txt",
        "input/unsorted_10.txt",
    ]
    
    for i in range(0, 10):
        list = OpenAndRead(filenames[i])
        sorted_list = sorted(list)
        matrix.append(sorted_list)
        i += 1

async def sort(matrix):
    index = []
    for i in range(0,10):
        index.append(0)
    arr = []
    while len(matrix) > 0:
        arr = getArr(matrix,index)
        for j in range (0, len(index)):
            if arr[j] == min(arr):
                merge_list.append(arr[j])
                index[j] += 1
                if index[j] == 100:
                    index.remove(index[j])
                    matrix.remove(matrix[j])
                break
            j += 1
    return merge_list

def getArr(matrix, index):
    arr = []
    for i in range(0,len(index)):
        arr.append(matrix[i][index[i]])
        i +=1
    return arr
 
if __name__ == '__main__':
    starttime = datetime.datetime.now()
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(getMatrix())
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(sort(matrix))
    print(merge_list)
    f = open("output/sorted.txt", "w")
    for i in range (0, len(merge_list)):
         f.write(f"{merge_list[i]}\n")
    f.close()
    endtime = datetime.datetime.now()
    time = endtime - starttime
    f = open("async_time.txt","w")
    f.write(f"{time}\n")
    f.close()
    