import numpy as np
import tkinter as tk
import threading
from tkinter import scrolledtext, messagebox
from tkinter.constants import END, INSERT, DISABLED, NORMAL
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk 

from utils import Data

def do_job():
    print('I am here')

db = Data()

def get_data():
    data = np.ones(12) * 22
    data = data + np.random.randint(low = 0, high = 10, size = (12,)) * 3
    db.store(data)
    timer0 = threading.Timer(2, get_data)
    timer0.start()

def update_data():
    global data
    data = db.get_new()
    # print('data =', data)
    timer1 = threading.Timer(2, update_data)
    timer1.start()

def _HelpDoc():
    DocGUI = tk.Tk()
    DocGUI.title('帮助文档')
    DocGUI.geometry("500x500")
    doc = scrolledtext.ScrolledText(DocGUI, width = 68, height = 38, relief = 'solid')
    doc.grid(column=0, row=0)
    DocGUI.mainloop()

def _info():
    str = '智能电子设备开发-分布式检测系统GUI\n开发者：赵泓珏\n开发时间：2021.10.26'
    messagebox.showinfo("关于", str)

def _SaveData():
    db.save()

def _Refresh():
    db.clear()


class Curve:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.geometry('800x600')
        self.root.title('曲线绘制')
        self.chose_node = [True, False, False, False]
        self.chose_param = [False, False, False]
        self.first_click = False
        
        self.AddMenu()
        self.CreatWidgets()
        self.RefreshFigure()

        
    def CreatWidgets(self):
        fig = Figure(figsize = (7, 7), dpi = 100)
        self.ax = fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(fig, self.root)
        self.canvas.get_tk_widget().pack(side = 'left', fill = 'y', expand=0)
        self.canvas._tkcanvas.pack(side = 'left', fill = 'y', expand=0)

        toolbar = NavigationToolbar2Tk(self.canvas, self.root)
        toolbar.update()


    def AddMenu(self):
        self.menubar = tk.Menu(self.root)                  
        
        self.StartMenu = tk.Menu(self.menubar, tearoff = False)
        self.StartMenu.add_command(label = '重置', command = self.Refresh)
        self.StartMenu.add_command(label = '保存图片', command = do_job)
        self.StartMenu.add_separator()
        self.StartMenu.add_command(label = '退出', command = self.quit)
        self.menubar.add_cascade(label='开始(S)', menu = self.StartMenu)

        self.ViewMenu1 = tk.Menu(self.menubar, tearoff = False)
        self.ViewMenu1.add_command(label = '节点1', command = self.click_node_1)
        self.ViewMenu1.add_command(label = '节点2', command = self.click_node_2)
        self.ViewMenu1.add_command(label = '节点3', command = self.click_node_3)
        self.ViewMenu1.add_command(label = '节点4', command = self.click_node_4)
        self.menubar.add_cascade(label='选择节点', menu = self.ViewMenu1)

        self.ViewMenu2 = tk.Menu(self.menubar, tearoff = False)
        self.ViewMenu2.add_command(label = '温度', command = self.click_param_1)
        self.ViewMenu2.add_command(label = '湿度', command = self.click_param_2)
        self.ViewMenu2.add_command(label = '光强', command = self.click_param_3)
        self.menubar.add_cascade(label='选择参数', menu = self.ViewMenu2)

        self.root['menu'] = self.menubar

    def draw(self):
        x = np.linspace(0, np.pi, 30)
        y = np.sin(x)
        self.ax.clear()
        self.ax.plot(x, y)
        self.canvas.draw()

    def RefreshFigure(self):
        legends_all = ['1 T', '1 H', '1 L', '2 T', '2 H', '2 L', '3 T', '3 H', '3 L', '4 T', '4 H', '4 L']
        legends = ['1 T', '1 H', '1 L', '2 T', '2 H', '2 L', '3 T', '3 H', '3 L', '4 T', '4 H', '4 L']
        d = db.df.iloc[:, 1:].values
        
        if self.chose_node[0]:
            d = db.get_node(1).values
            legends = legends_all[0:3]
        elif self.chose_node[1]:
            d = db.get_node(2).values
            legends = legends_all[3:6]
        elif self.chose_node[2]:
            d = db.get_node(3).values
            legends = legends_all[6:9]
        elif self.chose_node[3]:
            d = db.get_node(4).values
            legends = legends_all[9:]

        elif self.chose_node[0]:
            d = db.get_param('T').values
            legends = [legends_all[0], legends_all[3], legends_all[6], legends_all[9]]
        elif self.chose_node[1]:
            d = db.get_param('H').values
            legends = [legends_all[1], legends_all[4], legends_all[7], legends_all[10]]
        elif self.chose_node[2]:
            d = db.get_param('L').values
            legends = [legends_all[2], legends_all[5], legends_all[8], legends_all[11]]
        
        
        self.ax.clear()
        # for i in range(d.shape[1]):
        #     print(legends[i])
        #     self.ax.plot(d[:, i], label = legends[i])
        # print(legends)
        self.ax.plot(d)
        # print(lines)
        # plt.legend(lines, legends)
        self.canvas.draw()
        self.root.after(2, self.RefreshFigure)

    def quit(self):
        pass
    
    def Refresh(self):
        self.chose_node = [True, False, False, False]
        self.chose_param = [False, False, False]

    def click_node_1(self):
        self.chose_node = [True, False, False, False]
        self.chose_param = [False, False, False]
    
    def click_node_2(self):
        self.chose_node = [False, False, False, False]
        self.chose_node[1] = True
        self.chose_param = [False, False, False]

    def click_node_3(self):
        self.chose_node = [False, False, False, False]
        self.chose_node[2] = True
        self.chose_param = [False, False, False]

    def click_node_4(self):
        self.chose_node = [False, False, False, False]
        self.chose_node[3] = True
        self.chose_param = [False, False, False]

    def click_param_1(self):
        self.chose_param = [False, False, False]
        self.chose_param[0] = True
        self.chose_node = [False, False, False, False]

    def click_param_2(self):
        self.chose_param = [False, False, False]
        self.chose_param[1] = True
        self.chose_node = [False, False, False, False]

    def click_param_3(self):
        self.chose_param = [False, False, False]
        self.chose_param[2] = True
        self.chose_node = [False, False, False, False]

def CreateCurve():
    curve = Curve()
    curve.root.mainloop()

timer0 = threading.Timer(0.5, get_data)
timer0.daemon = True
timer1 = threading.Timer(0.5, update_data)
timer1.daemon = True

class MainGUI:
    def __init__(self):
        # 窗口设置
        self.Width = 390            # 窗口宽度
        self.Height = 360           # 窗口高度

        self.root = tk.Tk()         
        self.root.geometry(str(self.Width) + 'x' + str(self.Height))
        self.root.title('分布式环境监测系统')

        self.AddTxt()
        self.AddMenu()

        timer0.start()
        timer0.join()
        timer1.start()
        timer1.join()

        self.RefreshTxt()
        self.root.mainloop()

    def AddTxt(self):
        self.txt = scrolledtext.ScrolledText(self.root, width = 50, height = 3)
        self.txt.config(state = DISABLED)
        self.txt.grid(column=0, row=0)

    def RefreshTxt(self):
        global db
        a = db.get_new()[1]
        self.txt.config(state = NORMAL)
        self.txt.delete(1.0, END)
        self.txt.insert(INSERT, str(a))
        self.txt.config(state = DISABLED)
        self.root.after(1000, self.RefreshTxt)

    def AddMenu(self):
        self.menubar = tk.Menu(self.root)                  
        
        self.StartMenu = tk.Menu(self.menubar, tearoff = False)
        self.StartMenu.add_command(label = '刷新', command = self.Refresh)
        self.StartMenu.add_command(label = '保存数据', command = self.SaveData)
        self.StartMenu.add_command(label = '设置节点', command = do_job)
        self.StartMenu.add_separator()
        self.StartMenu.add_command(label = '退出', command = self.quit)
        self.menubar.add_cascade(label='开始(S)', menu = self.StartMenu)

        self.ViewMenu = tk.Menu(self.menubar, tearoff = False)
        self.ViewMenu.add_command(label = '绘制曲线', command = self.Curve)
        self.menubar.add_cascade(label='查看(V)', menu = self.ViewMenu)

        self.HelpMenu = tk.Menu(self.menubar, tearoff = False)
        self.HelpMenu.add_command(label = '文档', command = self.HelpDoc)
        self.HelpMenu.add_command(label = '关于', command = self.info)
        self.menubar.add_cascade(label='帮助(H)', menu = self.HelpMenu)

        self.root['menu'] = self.menubar
    
    def HelpDoc(self):
        thread_HelpDoc = threading.Thread(target=_HelpDoc, name='HelpDoc')
        thread_HelpDoc.daemon = True
        thread_HelpDoc.start()

    def info(self):
        thread_info = threading.Thread(target=_info, name='info')
        thread_info.daemon = True
        thread_info.start()

    def Refresh(self):
        thread_refresh = threading.Thread(target=_Refresh, name = 'Refresh')
        thread_refresh.daemon = True
        thread_refresh.start()
        thread_refresh.join()
    
    def Curve(self):
        thread_curve = threading.Thread(target=CreateCurve, name = 'Curve')
        thread_curve.daemon = True
        thread_curve.start()

    def SaveData(self):
        thread_savedata = threading.Thread(target=_SaveData, name = 'SaveData')
        thread_savedata.daemon = True
        thread_savedata.start()

    def quit(self):
        timer0.cancel()
        timer1.cancel()
        db.save()
        self.root.quit()

if __name__ == '__main__':
    MainGUI() 