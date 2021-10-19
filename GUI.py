import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as mpl
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk

from utils import *

class GUI:
    def __init__(self):
        # 窗口设置
        self.Width = 1200           # 窗口宽度
        self.Height = 600           # 窗口高度

        self.root = tk.Tk()         
        self.root.geometry(str(self.Width) + 'x' + str(self.Height))
        
        # 画图
        self.canvas = tk.Canvas()   # 显示图形的画布
        self.figure = self.create_matplotlib()
        self.create_form(self.figure)

        # 数据存储
        self.data = Data()
        self.root.mainloop()

    def create_matplotlib(self):
        # 创建绘图对象
        pass

    def create_form(self, figure):
        self.canvas = FigureCanvasTkAgg(figure, self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        toolbar = NavigationToolbar2Tk(self.canvas, self.root)
        toolbar.update()
        self.canvas._tkcanvas.pack(side = tk.TOP, fill = tk.BOTH, expand = 1)

    
gui = GUI()


        


