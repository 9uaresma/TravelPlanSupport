from tkinter import *
from tkinter import ttk

class Application(ttk.Frame):   #フレーム生成用クラス Frameクラスを継承
    def __init__(self, master = None):  #コンストラクタ(インスタンス生成時に実行される処理)
        super().__init__(master,padding=0) #Frame(継承元)のコンストラクタを実行
        self.master.title("旅行プラン") # ウィンドウタイトル
        self.master.geometry("1200x200")     # ウィンドウサイズ(幅x高さ)
        #--------------------------------------------------------
        self.pack(expand=1, fill=BOTH)#Frameを配置
        
        for i in range(24):
            ttk.Label(self, text=str(i), relief=GROOVE).place(x=20*i, y=50)
        canvas=Canvas(self.master,height=200,width=960,bg='red')
        canvas.place(x=0, y=0)
        for i in range(24):
            canvas.create_rectangle(40*i, 0, 40*(i+1), 50,fill='gray')
        for i in range(24):
            canvas.create_rectangle(40*i, 50, 40*(i+1), 600,fill='green')
        for i in range(24):
            Label(self.master, text=str(i), relief=FLAT, bg='gray').place(x=40*i+12, y=20)

        #ttk.Separator(self,orient="horizontal").grid(row=0, column=0, sticky="ew")
        #ttk.Label(self, text="プラン1").grid(column=0, row=1)
        #ttk.Label(self, text="プラン2").grid(column=0, row=2)
        #ttk.Button(self, text="Quit", command=root.destroy).grid(column=1,columnspan=3, row=3)
        #txt = ttk.Entry(self,width=20).grid(column=0, row=4)


if __name__ == "__main__":
    root = Tk()
    app = Application(master = root)
    app.mainloop()
