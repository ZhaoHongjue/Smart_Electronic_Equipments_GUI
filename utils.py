import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time

# 画图
class Chart:
    def __init__(self):
        self.fig, self.ax = plt.subplots(1, 1)
    
    def plot(self, data, pattern, name = None):
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
        if name is None:
            name = time.strftime("%Y%m%d%H%M%S", time.localtime())
        plt.savefig('./fig/' + name + '.png',bbox_inches='tight')

# 存储数据
class Data:
    def __init__(self):
        self.i = 0
        self.df = pd.DataFrame(columns=['time', '1_T','1_H','1_L',
                                        '2_T','2_H','2_L',
                                        '3_T','3_H','3_L',
                                        '4_T','4_H','4_L',])

    def store(self, *args):
        self.df.loc[self.i] = args
        self.i = self.i + 1

    def get(self, num):
        return self.df[['time', str(num) + '_T', str(num) + '_H', str(num) + '_L']]

    def clear(self, save = True):
        if save:
            self.save()
        self.df = pd.DataFrame(columns=['time','1_T','1_H','1_L',
                                        '2_T','2_H','2_L',
                                        '3_T','3_H','3_L',
                                        '4_T','4_H','4_L',])
        self.i = 0

    def save(self, name = None):
        if name is None:
            name = time.strftime("%Y%m%d%H%M%S", time.localtime())
        self.df.to_csv('./data/' + name + '.csv')

    def load(self, name = 'test'):
        self.df = pd.read_csv('/data/' + name + '.csv', index_col = 0)