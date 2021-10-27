import tkinter as tk
from tkinter import ttk
import threading, time, sys, queue
 
def fmtTime(timeStamp):
    timeArray = time.localtime(timeStamp)
    dateTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return dateTime
 
class GUI():
    def __init__(self, root):
        #new 一个Quue用于保存输出内容
        self.msg_queue = queue.Queue()
        self.initGUI(root)
    #在show_msg方法里，从Queue取出元素，输出到Text
    def show_msg(self):
        while not self.msg_queue.empty():
            content = self.msg_queue.get()
            self.text.insert("insert", content)
            self.text.see("end")
        #after方法再次调用show_msg
        self.root.after(100, self.show_msg)
 
    def initGUI(self, root):
        self.root = root
        self.root.title("test")
        self.root.geometry("400x200+700+500")
        self.root.resizable = False
    
        self.btn = ttk.Button(self.root, text="click", 
                              takefocus=0, command=self.show)
        self.btn.pack(side="top")
 
        self.scrollBar = ttk.Scrollbar(self.root)
        self.scrollBar.pack(side="right", fill="y")
 
        self.text = tk.Text(self.root, height=10, bd=1, relief="solid", 
                            yscrollcommand=self.scrollBar.set)
        self.text.pack(side="top", fill="both", padx=10, pady=10)
        self.scrollBar.config(command=self.text.yview)
 
        #启动after方法
        self.root.after(100, self.show_msg)
 
        root.mainloop()
 
    def __show(self):
        i = 0
        while i < 3:
            # print(fmtTime(time.time()))
            self.msg_queue.put(fmtTime(time.time())+"\n")
            time.sleep(1)
            i += 1
 
    def show(self):
        T = threading.Thread(target=self.__show, args=())
        T.start()
 
if __name__ == "__main__":
    root = tk.Tk()
    myGUI = GUI(root)