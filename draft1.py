from tkinter import *
from tkinter import ttk

COLOR_OF_TIME_AXIS = 'gray'
COLOR_OF_TIME_TABLE = 'green'

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
        #タイムテーブル
        frame_TimeTable=Frame(self, relief=FLAT,bg='red',width=1000,height=100) # FrameクラスからFrame_TimeTableインスタンスを生成
        frame_TimeTable.grid(row=0,column=0)
        
        #時間軸
        frame_TimeTable_TimeAxis=Frame(frame_TimeTable, relief=FLAT,bg='blue') # Frameクラスからframe_TimeTable_TimeAxisインスタンスを生成
        frame_TimeTable_TimeAxis.place(x=0,y=0)
        frame_TimeTable_TimeAxis_letter=[]
        label_time_l=[]
        for i in range(25):
            frame_TimeTable_TimeAxis_letter.append(Canvas(frame_TimeTable_TimeAxis,height=20,width=40,bg='blue',highlightthickness=0))
            frame_TimeTable_TimeAxis_letter[i].grid(row=0,column=i)
            frame_TimeTable_TimeAxis_letter[i].pack_propagate(0) #文字サイズに合わせて親オブジェクトのサイズが変わることを防ぐ
            frame_TimeTable_TimeAxis_letter[i].create_rectangle(0, 0, 40, 20,fill=COLOR_OF_TIME_AXIS,width=0)           
            label_time_l.append(Label(frame_TimeTable_TimeAxis_letter[i], text=str(i),bg=COLOR_OF_TIME_AXIS,font=("",'10')))
            label_time_l[i].pack(anchor='center',expand=1)
        del i
        
        #時間帯表示エリア
        frame_TimeTable_Table=Frame(frame_TimeTable, relief=FLAT,bg='blue')
        frame_TimeTable_Table.place(x=20,y=20)
        frame_TimeTable_Table_rect=[]
        for i in range(24):
            frame_TimeTable_Table_rect.append(Canvas(frame_TimeTable_Table,height=40,width=40,bg='yellow',highlightthickness=0))
            frame_TimeTable_Table_rect[i].grid(row=0,column=i)
            frame_TimeTable_Table_rect[i].create_rectangle(0, 0, 40, 40,fill=COLOR_OF_TIME_TABLE)       
        del i

if __name__ == "__main__":
    root = Tk()
    app = Application(master = root)
    app.mainloop()
