 from tkinter import *
from tkinter import messagebox
import time
 
class Ball:
    #def __init__(self, canvas, color, tk):
    def __init__(self, canvas1, canvas2, color, tk):
        self.canvas1 = canvas1
        self.canvas2=canvas2
        self.tk=tk
        self.id=canvas2.create_oval(0,0,50,50, fill=color, tag="Ball")
        self.step = 5
        scale = Scale(canvas1, command=self.print__scale,orient="horizontal", tickinterval=5, from_=5, to=50)
        scale.pack()
        self.scale = scale
        self.x=self.step
        self.y=self.step
        self.tk.protocol("WM_DELETE_WINDOW", self.ask_quit)
        self.tk.bind("<Left>", self.change_direction)
        self.tk.bind("<Right>", self.change_direction)
        self.tk.bind("<Up>", self.change_direction)
        self.tk.bind("<Down>", self.change_direction)
        self.tk.bind("<Escape>", self.change_direction)
    
    def ask_quit(self):
        result = messagebox.askquestion("Mesage", "Quit")
        if result == "yes":
            self.tk.destroy()
 
    def change_direction(self, event):
        if event.keysym == "Left":
            #DX = -STEP; DY = 0
            self.x=-self.step; self.y=0
        elif event.keysym == "Right":
            #DX = STEP; DY = 0
            self.x=self.step; self.y=0
        elif event.keysym == "Up":
            #DX = 0; DY = -STEP
            self.x=0; self.y=-self.step
        elif event.keysym == "Down":
            #DX = 0; DY = STEP
            self.x=0; self.y=self.step
        elif event.keysym == "Escape":
            self.x=self.step; self.y=self.step
    def print__scale(self, var):
            self.step = int(var)
            self.x=self.step
            self.y=self.step
            print(self.step)
    def draw(self):
        self.canvas2.move(self.id,self.x,self.y)
        pos=self.canvas2.coords(self.id)
        temp=0
        if pos[1]<=0:
            temp=self.y*-1
            self.y = temp
            temp = 0
        if pos[3]>=self.canvas2.winfo_height():
            temp=self.y*-1
            self.y = temp
            temp = 0
        if pos[0]<=0:
            temp=self.x*-1
            self.x = temp
            temp = 0
        if pos[2]>=self.canvas2.winfo_width():
            temp=self.x*-1
            self.x = temp
            temp = 0
        self.canvas2.update_idletasks()
        self.canvas2.update()
        self.canvas2.after(50, self.draw)
 
if __name__ == "__main__":
    tk=Tk()
    tk.title('BOUNCE')
    label1 = LabelFrame(tk, text="Simulation Parameters", width = 400, height=100, fg="red", relief="solid")
    label2 = LabelFrame(tk, text="Bouncing Ball", width=400, height=300, fg="red", relief="solid")
    label1.pack()
    label2.pack()
    canvas1=Canvas(label1,width=450,height=550,bd=0,highlightthickness=0)
    canvas1.pack(expand=YES, fill=BOTH)
    canvas2=Canvas(label2,width=450,height=550,bd=0,highlightthickness=0)
    canvas2.pack(expand=YES, fill=BOTH)
    
    tk.update()
    #ball=Ball(canvas,'red', tk)
    ball=Ball(canvas1, canvas2, 'red', tk)
    ball.draw()
    time.sleep(0.01)
    mainloop()
