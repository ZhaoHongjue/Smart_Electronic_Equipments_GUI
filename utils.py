import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 画图
class Chart:
    def __init__(self):
        self.fig, self.ax = plt.subplots(1, 1)
    
    def plot(self, episode_rewards):
        self.ax.clear()
        self.ax.plot(episode_rewards)
        self.ax.set_xlabel('iteration')
        self.ax.set_ylabel('episode reward')
        self.fig.canvas.draw()

# 存储数据
class Data:
    def __init__(self):
        self.capacity = 10000
        self.i = 0
        self.count = 0
        self.df = pd.DataFrame(index=range(self.capacity),
                               columns=['节点1温度','节点1湿度','节点1光照',
                                        '节点2温度','节点2湿度','节点2光照',
                                        '节点3温度','节点3湿度','节点3光照'])
    def store(self, *args):
        self.memory.loc[self.i] = args

    def clear(self):
        pass

    def save(self):
        self.df.to_csv('test.csv')