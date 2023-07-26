import time
import threading
import asyncio
from multiprocessing import Process


def cal_average(num):  
  sum_num = 0
  for t in num:
    sum_num = sum_num + t
  avg = sum_num / len(num)
  time.sleep(1)
  return avg

def main_sequential(list1, list2, list3):  
  s = time.perf_counter()
  # your code goes here
  cal_average(list1)
  cal_average(list2)
  cal_average(list3)


  elapsed = time.perf_counter() - s
  print("Sequential Programming Elapsed Time: " + str(elapsed) + " seconds")

async def cal_average_async(num):  
  sum_num = 0
  for t in num:
    sum_num = sum_num + t
  avg = sum_num / len(num)
  await asyncio.sleep(1)
  return avg

async def main_async(list1, list2, list3):  
  s = time.perf_counter()
  # your code goes here
  tasks = [cal_average_async(list1), cal_average_async(list2), cal_average_async(list3)]
  await asyncio.gather(*tasks)

  elapsed = time.perf_counter() - s
  print("Asynchronous Programming Elapsed Time: " + str(elapsed) + " seconds")

def main_threading(list1, list2, list3):  
  s = time.perf_counter()
  lists = [list1, list2, list3]
  threads = []
  for i in range(len(lists)):
    x = threading.Thread(target=cal_average, args=(lists[i],))
    threads.append(x)
    x.start()
    for x in threads:
      x.join()


  elapsed = time.perf_counter() - s
  print("Threading Elapsed Time: " + str(elapsed) + " seconds")

def main_multiprocessing(list1, list2, list3):  
  s = time.perf_counter()
  lists = [list1, list2, list3] 
  processes = [Process(target=cal_average, args=(lists[i],)) for i in range(len(lists))]
  for p in processes:
    p.start()
  for p in processes:
    p.join()


  elapsed = time.perf_counter() - s
  print("Multiprocessing Elapsed Time: " + str(elapsed) + " seconds")


