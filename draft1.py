from tkinter import *
from tkinter import ttk

COLOR_OF_TIME_AXIS = 'gray'
COLOF_OF_TIME_TABLE = 'green'

class Application(ttk.Frame):   #メインフレーム Frameクラスを継承
    def __init__(self, master = None):  #コンストラクタ(インスタンス生成時に実行される処理)
        super().__init__(master) #Frame(継承元)のコンストラクタを実行.親ウィジェットを設定
        #ウインドウの設定
        self.master.title("旅行プラン") # ウィンドウタイトル
        self.master.geometry("1200x200")     # ウィンドウサイズ(幅x高さ)
        #MainFrameを配置
        self.pack(expand=1, fill=BOTH)
        #--------------------------------------------------------
        #以下、子ウイジェットを記述
        #時間軸
        frame_TimeAxis=Frame(self, relief=FLAT,width=960,height=40,bg='red') # FrameクラスからFrame_TimeAxisインスタンスを生成
        frame_TimeAxis.place(relx=0, rely=0) # Frame_TimeAxisフレームを配置
        frame_TimeAxis_letter=[]
        for i in range(24):
            frame_TimeAxis_letter.append(Frame(frame_TimeAxis, relief=FLAT, bd=5, width=40,height=40,bg=COLOR_OF_TIME_AXIS))
            frame_TimeAxis_letter[i].pack_propagate(0)  #親フレームサイズの固定。pack時のフレームサイズ自動変更を防ぐ
            frame_TimeAxis_letter[i].place(x=40*i, y=0)
            label_time_1=Label(frame_TimeAxis_letter[i], text=str(i),bg=COLOR_OF_TIME_AXIS,font='20')
            label_time_1.pack(anchor='center',expand=1)
        
        #背景
        canvas=Canvas(self,height=150,width=960)
        canvas.place(x=0, y=40)
        for i in range(24):
            canvas.create_rectangle(40*i, 0, 40*(i+1), 600,fill=COLOF_OF_TIME_TABLE)


if __name__ == "__main__":
    root = Tk()
    app = Application(master = root)
    app.mainloop()
