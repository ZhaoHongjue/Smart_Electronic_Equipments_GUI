import tkinter as tk
import matplotlib
from matplotlib import figure
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as mpl
import pandas as pd
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk

from utils import *

class CurveGUI:
    def __init__(self):
        # 窗口设置
        self.Width = 1200           # 窗口宽度
        self.Height = 600           # 窗口高度

        self.root = tk.Tk()         
        self.root.geometry(str(self.Width) + 'x' + str(self.Height))
        self.root.title('分布式环境监测系统')

        self.data = Data()
        
        # self.createLabels()
        self.creatWidgets()
        
        self.root.mainloop()

    def creatWidgets(self):
        fig = Figure(figsize = (7, 7), dpi = 100)
        self.ax = fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(fig, self.root)
        self.canvas.get_tk_widget().pack(side = 'left', fill = 'y', expand=0)
        self.canvas._tkcanvas.pack(side = 'left', fill = 'y', expand=0)

        toolbar = NavigationToolbar2Tk(self.canvas, self.root)
        toolbar.update()

        # footframe = tk.Frame(master = self.root).pack(side=tk.BOTTOM)
        # tk.Button(master=footframe, text='重画', command = self.draw).pack(side=tk.BOTTOM)
        # tk.Button(master=footframe, text = '退出', command = self.quit).pack(side = tk.BOTTOM)
    
    def createLabels(self):
        lblframe = tk.Frame(master = self.root).pack(side=tk.RIGHT)
        tk.Label(master=lblframe, text = '节点1').pack(padx=10, pady=80)
        tk.Label(master=lblframe, text = '节点2').pack(padx=10, pady=20)

        # lbl1 = tk.Label(self.root, text = '节点1')
        # lbl1.grid(column=0, row=0)

    def draw(self):
        x = np.linspace(0, np.pi, 30)
        y = np.sin(x)
        self.ax.clear()
        self.ax.plot(x, y)
        self.canvas.draw()

    def quit(self):
        self.root.quit()
        self.root.destroy()
if __name__ == '__main__':
    gui = GUI()


        


