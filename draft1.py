from tkinter import *
from tkinter import ttk

class Application(ttk.Frame):   #フレーム生成用クラス Frameクラスを継承
    def __init__(self, master = None):  #コンストラクタ(インスタンス生成時に実行される処理)
        super().__init__(master,padding=10) #Frame(継承元)のコンストラクタを実行
        self.master.title("旅行プラン")
        self.grid() #Frameを配置
        for i in range(24):
            ttk.Label(self, text=str(i), relief=GROOVE).grid(column=i+1, row=0, padx=0)
        ttk.Separator(self,orient="horizontal").grid(row=0, column=0, sticky="ew")
        ttk.Label(self, text="プラン1").grid(column=0, row=1)
        ttk.Label(self, text="プラン2").grid(column=0, row=2)
        ttk.Button(self, text="Quit", command=root.destroy).grid(column=1,columnspan=3, row=3)
        txt = ttk.Entry(self,width=20).grid(column=0, row=4)


if __name__ == "__main__":
    root = Tk()
    app = Application(master = root)
    app.mainloop()
