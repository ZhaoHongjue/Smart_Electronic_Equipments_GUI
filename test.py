# import threading
# import time

# def thread_job():
#     global temp
#     print("T1 start\n")
#     for i in range(10):
#         time.sleep(0.1) # 任务间隔0.1s
#         temp.append(i)
#     print("T1 finish\n")
#     added_thread = threading.Timer(1, thread_job)
#     added_thread.start()
#     # added_thread.join()

# def main():
#     global temp
#     while True:
#         print(temp)

# temp = []

# if __name__ == '__main__':
#     added_thread = threading.Timer(1, thread_job)
#     added_thread.daemon = True
#     added_thread.start()
#     added_thread.join()
#     main()

import tkinter 
import numpy as np

VarList = np.zeros((12,), dtype=tkinter.IntVar)
print(VarList, type(VarList), type(VarList[0]))
for i in range(len(VarList)):
    VarList[i].get()
    VarList[i] = i
print(VarList)