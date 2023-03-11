from tkinter import *
from tkinter import ttk
import math

COLOR_OF_TIME_AXIS = 'white'
COLOR_OF_TIME_TABLE = 'green'

#入力値
time_from=2.5
time_to=4

class Application(ttk.Frame):   #メインフレーム Frameクラスを継承  
    class InputTable:
        InputTableNum = 0
        InputTableList = []
        class RectGeneration:
            def __init__(self):                  # コンストラクタ
                self.canv = None
                self.rect_exist=False
            def DrawRect(self, parent_frame, ent_from_time, ent_from_minute, ent_to_time, ent_to_minute):
                def inner():
                    if self.canv==None:
                        if str.isdigit(ent_from_time.get()) and str.isdigit(ent_from_minute.get()) and str.isdigit(ent_to_time.get()) and str.isdigit(ent_to_minute.get()):
                            #開始時刻[分]
                            start_minute = int(ent_from_time.get())*60 + int(ent_from_minute.get())
                            #終了時刻[分]
                            end_minute = int(ent_to_time.get())*60 + int(ent_to_minute.get())
                            #矩形width計算
                            rect_width=(end_minute - start_minute)*40/60
                            print(rect_width)
                            rect_return=Canvas(parent_frame, relief=FLAT,bg='gold',width=rect_width,height=20,highlightthickness=0)
                            rect_return.place(x=start_minute*40/60,y=0) 
                            self.canv = rect_return
                            self.rect_exist=True
                            print(self.canv)
                        else:
                            print("Enter Digits!")
                    else:
                        pass
                return inner
            def RmRect(self):
                def inner():
                    if self.canv!=None:
                        self.canv.destroy()
                        self.canv=None
                        self.rect_exist=False
                        print(self.canv)
                    else:
                        print(self.canv)
                return inner        

        def __init__(self,ParentFrame,frame_TimeTable_Table):                  # コンストラクタ
            
            #入力部
            
            label_title=Label(ParentFrame,text="タイトル",bg=COLOR_OF_TIME_AXIS,font=("",'10'))
            label_title.grid(row=0,column=0)

            ent_label_title=Entry(ParentFrame,width=20)
            ent_label_title.grid(row=0,column=1)        

            label_TimeInput_from=Label(ParentFrame,text="出発",bg=COLOR_OF_TIME_AXIS,font=("",'10'))
            label_TimeInput_from.grid(row=0,column=2)
            
            ent_TimeInput_from_time=Entry(ParentFrame,width=5)
            ent_TimeInput_from_time.grid(row=0,column=3)

            label_TimeInput_from_time=Label(ParentFrame,text="時",bg=COLOR_OF_TIME_AXIS,font=("",'10'))
            label_TimeInput_from_time.grid(row=0,column=4)

            ent_TimeInput_from_minute=Entry(ParentFrame,width=5)
            ent_TimeInput_from_minute.grid(row=0,column=5)

            label_TimeInput_from_minute=Label(ParentFrame,text="分",bg=COLOR_OF_TIME_AXIS,font=("",'10'))
            label_TimeInput_from_minute.grid(row=0,column=6)
            
            label_TimeInput_to=Label(ParentFrame,text="到着",bg=COLOR_OF_TIME_AXIS,font=("",'10'))
            label_TimeInput_to.grid(row=0,column=7)

            ent_TimeInput_to_time=Entry(ParentFrame,width=5)
            ent_TimeInput_to_time.grid(row=0,column=8)

            label_TimeInput_to_time=Label(ParentFrame,text="時",bg=COLOR_OF_TIME_AXIS,font=("",'10'))
            label_TimeInput_to_time.grid(row=0,column=9)

            ent_TimeInput_to_minute=Entry(ParentFrame,width=5)
            ent_TimeInput_to_minute.grid(row=0,column=10)

            label_TimeInput_minute=Label(ParentFrame,text="分",bg=COLOR_OF_TIME_AXIS,font=("",'10'))
            label_TimeInput_minute.grid(row=0,column=11)
            
            rect_timetable=self.RectGeneration()
            button_Time = Button(ParentFrame, text="Enter",command=rect_timetable.DrawRect(frame_TimeTable_Table, 
                                                                                    ent_TimeInput_from_time,
                                                                                    ent_TimeInput_from_minute,
                                                                                    ent_TimeInput_to_time,
                                                                                    ent_TimeInput_to_minute,
                                                                                    ))
            button_Time.grid(row=0,column=12)
            button_remove = Button(ParentFrame, text="Remove",command=rect_timetable.RmRect())
            #button_remove = Button(ParentFrame, text="Enter",command=self.RemoveWidget_place(rect))
            button_remove.grid(row=0,column=13)
    
    def ApendInputTable(self, ParentFrame, frame_TimeTable_Table,frame_button_TimeInput):
        def inner():                
            self.InputTable.InputTableList.append(Frame(ParentFrame, relief=FLAT,bg='gray',width=1000,height=100))
            self.InputTable.InputTableList[-1].grid(row=self.InputTable.InputTableNum+1,column=0, columnspan=2)
            self.InputTable(self.InputTable.InputTableList[-1],frame_TimeTable_Table)
            frame_button_TimeInput.grid_forget()   
            frame_button_TimeInput.grid(row=self.InputTable.InputTableNum + 2,column=0,sticky=N)
            self.InputTable.InputTableNum = self.InputTable.InputTableNum + 1
        return inner
    
    def RmInputTable(self):
        def inner(): 
            if self.InputTable.RectGeneration.rect_exist:
                print("exist rect")
            else:
                self.InputTable.InputTableList[-1].grid_forget()
                self.InputTable.InputTableList.pop()
        return inner

    def __init__(self, master = None):  #コンストラクタ(インスタンス生成時に実行される処理)
        super().__init__(master) #Frame(継承元)のコンストラクタを実行.親ウィジェットを設定
        #ウインドウの設定
        self.master.title("旅行プラン") # ウィンドウタイトル
        self.master.geometry("1200x400")     # ウィンドウサイズ(幅x高さ)
        #MainFrameを配置
        self.pack(expand=1, fill=BOTH)
        #--------------------------------------------------------
        #以下、子ウイジェットを記述
        #タイムテーブル
        frame_TimeTable=Frame(self, relief=FLAT,bg='gray',width=1000,height=300) # FrameクラスからFrame_TimeTableインスタンスを生成
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
        #入力部
        frame_TimeInput=Frame(self, relief=FLAT,bg='blue',width=1000,height=100)
        frame_TimeInput.place(x=0,y=70)
        frame_TimeInput_base=Frame(frame_TimeInput, relief=FLAT,bg='yellow',width=1000,height=10)
        frame_TimeInput_base.grid(row=0,column=0,columnspan=2)

        frame_button_TimeInput=Frame(frame_TimeInput,bg='red')
        frame_button_TimeInput.grid(row=1,column=0)

        button_TimeInput_Ap = Button(frame_button_TimeInput)
        button_TimeInput_Ap.configure(text="追加", command=self.ApendInputTable(frame_TimeInput,frame_TimeTable_Table,frame_button_TimeInput))
        button_TimeInput_Ap.grid(row=0,column=0)

        button_TimeInput_Rm = Button(frame_button_TimeInput)
        button_TimeInput_Rm.configure(text="削除", command=self.RmInputTable())
        button_TimeInput_Rm.grid(row=0,column=1)


if __name__ == "__main__":
    root = Tk()
    app = Application(master = root)
    app.mainloop()
