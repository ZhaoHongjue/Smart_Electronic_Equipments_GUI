import time
import threading
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from utils import Data
from CurveGUI import CurveGUI
import numpy as np

VarList = np.zeros(12)

def get_data():
    data = np.ones(12) * 22
    data = data + np.random.randint(low = 0, high = 10, size = (12,)) * 3
    return data

def update_data():
    global VarList
    VarList = get_data()
    timer_update = threading.Timer(5, update_data)
    timer_update.start()
    
def Curve():
    CurveGUI()

def do_job():
    print('I am here')

timer_update = threading.Timer(5, update_data)
timer_update.daemon = True
thread_curve = threading.Thread(target=Curve, name='Plot')
thread_curve.daemon = True

class MainGUI:
    def __init__(self):
        self.data = Data()

        # 窗口设置
        self.Width = 390            # 窗口宽度
        self.Height = 360           # 窗口高度

        self.root = Tk()         
        self.root.geometry(str(self.Width) + 'x' + str(self.Height))
        self.root.title('分布式环境监测系统')

        self.AddMenu()
        timer_update.start()
        timer_update.join()
        self.AddLabel()
        
        self.root.mainloop()
    
    def AddMenu(self):
        time.sleep(2)
        self.menubar = Menu(self.root)                  
        
        self.StartMenu = Menu(self.menubar, tearoff = False)
        self.StartMenu.add_command(label = '保存数据', command = do_job)
        self.StartMenu.add_command(label = '载入数据', command = do_job)
        self.StartMenu.add_command(label = '设置节点', command = do_job)
        self.StartMenu.add_separator()
        self.StartMenu.add_command(label = '退出', command = self.root.quit)
        self.menubar.add_cascade(label='开始(S)', menu = self.StartMenu)

        # self.EditMenu = Menu(self.menubar, tearoff = False)
        # self.EditMenu.add_command(label = '1', command = do_job)
        # self.EditMenu.add_command(label = '2', command = do_job)
        # self.EditMenu.add_command(label = '3', command = do_job)
        # self.menubar.add_cascade(label='编辑(E)', menu = self.EditMenu)

        self.ViewMenu = Menu(self.menubar, tearoff = False)
        self.ViewMenu.add_command(label = '绘制曲线', command = self.DrawCurve)
        self.ViewMenu.add_command(label = '2', command = do_job)
        self.ViewMenu.add_command(label = '3', command = do_job)
        self.menubar.add_cascade(label='查看(V)', menu = self.ViewMenu)

        self.HelpMenu = Menu(self.menubar, tearoff = False)
        self.HelpMenu.add_command(label = '文档', command = self.HelpDoc)
        self.HelpMenu.add_command(label = '关于', command = self.info)
        self.menubar.add_cascade(label='帮助(H)', menu = self.HelpMenu)

        self.root['menu'] = self.menubar

    def AddLabel(self):
        global VarList
        lbl1 = Label(self.root, text="节点1", font=("黑体", 20))
        lbl1.grid(column = 0, row = 0)
        LT1 = Label(self.root, text = '温度：', font=("黑体", 15))
        LT1.grid(column=0, row=1)
        T1 = Label(self.root, text = str(VarList[0]) + ' ', font=("黑体", 15))
        T1.grid(column=1, row=1)
        LH1 = Label(self.root, text = '湿度：', font=("黑体", 15))
        LH1.grid(column=0, row=2)
        H1 = Label(self.root, text = str(VarList[1]) + ' ', font=("黑体", 15))
        H1.grid(column=1, row=2)
        LL1 = Label(self.root, text = '光照：', font=("黑体", 15))
        LL1.grid(column=0, row=3)
        L1 = Label(self.root, text = str(VarList[2]) + ' ', font=("黑体", 15))
        L1.grid(column=1, row=3)
        enter = Label(self.root, text="\n", font=("黑体", 10))
        enter.grid(column=0, row=4)

        lbl2 = Label(self.root, text="    节点2", font=("黑体", 20))
        lbl2.grid(column=2, row=0)
        LT2 = Label(self.root, text = '    温度：', font=("黑体", 15))
        LT2.grid(column=2, row=1)
        T2 = Label(self.root, text = str(VarList[3]) + ' ', font=("黑体", 15))
        T2.grid(column=3, row=1)
        LH2 = Label(self.root, text = '    湿度：', font=("黑体", 15))
        LH2.grid(column=2, row=2)
        H2 = Label(self.root, text = str(VarList[4]) + ' ', font=("黑体", 15))
        H2.grid(column=3, row=2)
        LL2 = Label(self.root, text = '    光照：', font=("黑体", 15))
        LL2.grid(column=2, row=3)
        L2 = Label(self.root, text = str(VarList[5]) + ' ', font=("黑体", 15))
        L2.grid(column=3, row=3)
        enter = Label(self.root, text="\n", font=("黑体", 10))
        enter.grid(column=2, row=4)

        lbl3 = Label(self.root, text="节点3", font=("黑体", 20))
        lbl3.grid(column = 0, row = 5)
        LT3 = Label(self.root, text = '温度：', font=("黑体", 15))
        LT3.grid(column=0, row=6)
        T3 = Label(self.root, text = str(VarList[6]) + ' ', font=("黑体", 15))
        T3.grid(column=1, row=6)
        LH3 = Label(self.root, text = '湿度：', font=("黑体", 15))
        LH3.grid(column=0, row=7)
        H3 = Label(self.root, text = str(VarList[7]) + ' ', font=("黑体", 15))
        H3.grid(column=1, row=7)
        LL3 = Label(self.root, text = '光照：', font=("黑体", 15))
        LL3.grid(column=0, row=8)
        L3 = Label(self.root, text = str(VarList[8]) + ' ', font=("黑体", 15))
        L3.grid(column=1, row=8)
        # enter = Label(self.root, text="\n", font=("黑体", 25))
        # enter.grid(column=0, row=9)

        lbl4 = Label(self.root, text="    节点4", font=("黑体", 20))
        lbl4.grid(column=2, row=5)
        LT4 = Label(self.root, text = '    温度：', font=("黑体", 15))
        LT4.grid(column=2, row=6)
        T4 = Label(self.root, text = str(VarList[9]) + ' ', font=("黑体", 15))
        T4.grid(column=3, row=6)
        LH4 = Label(self.root, text = '    湿度：', font=("黑体", 15))
        LH4.grid(column=2, row=7)
        H4 = Label(self.root, text = str(VarList[10]) + ' ', font=("黑体", 15))
        H4.grid(column=3, row=7)
        LL4 = Label(self.root, text = '    光照：', font=("黑体", 15))
        LL4.grid(column=2, row=8)
        L4 = Label(self.root, text = str(VarList[11]) + ' ', font=("黑体", 15))
        L4.grid(column=3, row=8)
        # enter = Label(self.root, text="\n", font=("黑体", 10))
        # enter.grid(column=2, row=9)
        VarList = []

    def HelpDoc(self):
        self.DocGUI = Tk()
        self.DocGUI.title('帮助文档')
        self.DocGUI.geometry("500x500")
        self.doc = scrolledtext.ScrolledText(self.DocGUI, width = 68, height = 38, relief = 'solid')
        self.doc.grid(column=0, row=0)
        self.DocGUI.mainloop()
    
    def info(self):
        str = '智能电子设备开发-分布式检测系统GUI\n开发者：赵泓珏\n开发时间：2021.10.26'
        messagebox.showinfo("关于", str)

    def DrawCurve(self):
        thread_curve.start()

def CreateGUI():
    MainGUI()

# thread_main = threading.Thread(target=CreateGUI, name='Main')
if __name__ == '__main__':
    CreateGUI()