from os import stat
from tkinter import ACTIVE, DISABLED, Tk, Canvas, Frame, Label, Button, messagebox
import winsound, time
from conts import Variables,Screen


class App(Tk):

    def __init__(self):
        super().__init__()

        self.b = Variables.b
        self.t = Variables.t
        self.lb = Variables.lb
        self.pomodro_cntr = Variables.pomodro_cntr

        self.resizable(width=Screen.MainScreen.resizable_x, height=Screen.MainScreen.resizable_y)
        self.title(Screen.MainScreen.title)

        self.main_canvas = Canvas(self, height=Screen.MainScreen.screen_height, width=Screen.MainScreen.screen_width, bg=Screen.MainScreen.bg)
        self.main_canvas.pack()

        self.main_frame = Frame(self, bg=Screen.MainScreen.bg)
        self.main_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.lbl_1= Label(self.main_frame,text="POMODRO",bg="black",fg="white",font="Times 25 bold")
        self.lbl_1.place(x=185,y=50)

        self.counter_lbl= Label(self.main_frame,text="25:00",bg="Black",fg="White",font="Times 100 italic")
        self.counter_lbl.place(x=115,y=100)

        self.lbl_pomodro= Label(text=f"TOPLAM POMODROLAR : {self.pomodro_cntr}",fg="White",bg="Black",font="Times 10 italic")
        self.lbl_pomodro.place(x=10,y=10)

        self.btn_study=Button(self.main_frame,text="Başla",activebackground="Darkgray",width=10,command=self.pomodro)
        self.btn_study.place(x=280,y=270)

        self.btn_break=Button(self.main_frame,text="Uzun Ara",activebackground="Darkgray",width=10,command=self.long_break)
        self.btn_break.place(x=195,y=270)

    def pomodro(self):
        self.lbl_1.config(text="ÇALIŞMA")
        self.lbl_1.place(x=200,y=50)
        if self.t>0:
            mins,secs=divmod(self.t,60)
            timer="{:02d}:{:02d}".format(mins,secs)
            self.counter_lbl.config(text=timer)
            self.t=self.t-1
            self.counter_lbl.after(1000,self.pomodro)
            self.btn_study.config(state=DISABLED)
            
        
        elif self.t==0:
            self.counter_lbl.config(text="00:00")
            winsound.Beep(800,500)
            self.pomodro_cntr+=1
            self.lbl_pomodro.config(text=f"TOPLAM POMODROLAR : {self.pomodro_cntr}")
            messagebox.showinfo("Bilgilendirme" , "ARA ZAMANI !!!")
            self.t=3
            self.pomodro_break()
            self.btn_study.config(state=ACTIVE)

    def pomodro_break(self):
        self.lbl_1.config(text="ARA")
        self.lbl_1.place(x=230,y=50)
        if self.b>0:
            mins,secs=divmod(self.b,60)
            timer="{:02d}:{:02d}".format(mins,secs)
            self.counter_lbl.config(text=timer)
            self.b=self.b-1
            self.counter_lbl.after(1000,self.pomodro_break)
            self.btn_study.config(state=DISABLED)
        elif self.b==0:
            
            self.counter_lbl.config(text="00:00")
            winsound.Beep(1000,700)
            messagebox.showinfo("Bilgilendirme" , "ÇALIŞMAYA DÖNME ZAMANI !!!")
            self.b=2
            self.btn_study.config(state=ACTIVE)

    def long_break(self):
        if self.pomodro_cntr==4:
            self.lbl_1.config(text="UZUN ARA")
            self.lbl_1.place(x=190,y=50)
            if self.lb>0:
                mins,secs=divmod(self.lb,60)
                timer="{:02d}:{:02d}".format(mins,secs)
                self.counter_lbl.config(text=timer)
                self.lb=self.lb-1
                self.counter_lbl.after(1000,self.long_break)
            elif self.lb==0:
                self.counter_lbl.config(text="00:00")
                winsound.Beep(300,1000)
                messagebox.showinfo("Bilgilendirme" , "ARA BİTTİ,ÇALIŞMAYA DÖNME ZAMANI !!!")
                self.lb=15
        elif self.pomodro_cntr!=4:
            messagebox.showerror("HATA","4 ADET POMODRO TAMAMLAMADAN UZUN ARA YAPAMAZSINIZ!!!")

def run():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    run()