import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time

# 存储数据
class Data:
    def __init__(self):
        self.i = 0
        self.df = pd.DataFrame(columns=['time', '1_T','1_H','1_L',
                                        '2_T','2_H','2_L',
                                        '3_T','3_H','3_L',
                                        '4_T','4_H','4_L',])

    def store(self, data):
        time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.df.loc[self.i, 'time'] = time_now
        self.df.iloc[self.i, 1:] = data[:]
        self.i = self.i + 1
    
    def get_new(self):
        return self.df.loc[self.i-1].values
    
    def get_node(self, node):
        return self.df[['time', str(node) + '_T', str(node) + '_H', str(node) + '_L']]

    def clear(self):
        self.save()
        self.df = pd.DataFrame(columns=['time','1_T','1_H','1_L',
                                        '2_T','2_H','2_L',
                                        '3_T','3_H','3_L',
                                        '4_T','4_H','4_L',])
        self.i = 0

    def save(self, name = 'test'):
        self.df.to_csv(name + '.csv')

    def load(self, name = 'test'):
        self.df = pd.read_csv(name + '.csv', index_col = 0)