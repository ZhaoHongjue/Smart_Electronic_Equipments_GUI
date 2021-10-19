import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 画图
class Chart:
    def __init__(self):
        self.fig, self.ax = plt.subplots(1, 1)
    
    def plot(self, data, pattern):
        self.ax.clear()
        self.ax.plot(data)
        
        # 设置坐标
        self.ax.set_xlabel('Time')
        if pattern == 1:
            self.ax.set_ylabel('Temperature')
        elif pattern == 2:
            self.ax.set_ylabel('Humidity')
        elif pattern == 3:
            self.ax.set_ylabel('Luminousintensity')
        self.fig.canvas.draw()

# 存储数据
class Data:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.i = 0
        self.count = 0
        self.df = pd.DataFrame(index=range(self.capacity),
                               columns=['1_T','1_H','1_L',
                                        '2_T','2_H','2_L',
                                        '3_T','3_H','3_L',
                                        '4_T','4_H','4_L',])
    def store(self, *args):
        self.df.loc[self.i] = args
        self.i = self.i + 1

    def clear(self):
        pass

    def save(self):
        self.df.to_csv('test.csv')

    def load(self):
        pass