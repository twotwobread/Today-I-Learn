from tkinter import *
from flask import Flask, render_template, request
import time
import json
from threading import Thread
RED, BLUE, GREEN = 0, 0, 0

webRemoteControlServer = Flask(__name__)

@webRemoteControlServer.route("/")
def index():
    return render_template('web.html')

@webRemoteControlServer.route("/rc_LED", methods=["POST"])
def request_data():
    global RED, GREEN, BLUE, app
    cmd=request.form.get("rc_LED")
    color, value = cmd.split()
    print("color = {}, value = {}".format(color, value))
    value =int(value)
    if color=="red":
        RED = value
        app.changeRed(value)
    elif color=="green":
        GREEN = value
        app.changeGreen(value)
    elif color=="blue":
        BLUE = value
        app.changeBlue(value)
    return json.dumps({'status':'OK'})

@webRemoteControlServer.route("/reset_LED", methods=["POST"])
def reset_LED():
    global RED, GREEN, BLUE
    cmd=request.form.get("reset_LED")
    red_value, green_value, blue_value = cmd.split()
    print("red = {}, green = {}, blue = {}".format(red_value, green_value, blue_value))
    RED=255
    GREEN = 255
    BLUE = 255
    return json.dumps({'status':'OK'})
class RemoteControl_Drawing:
    def __init__(self, win): 
        frame = Frame(win) 
        frame.pack()
        Label(frame, text="Checking RGB Color Combination").grid(row=0, column=0, columnspan=3)
        Label(frame, text='Red').grid(row=1, column=0)
        Label(frame, text='Green').grid(row=2, column=0)
        Label(frame, text='Blue').grid(row=3, column=0)

        self.red_var = IntVar()
        self.green_var = IntVar()
        self.blue_var = IntVar()
        self.red = 255
        self.green = 255
        self.blue = 255

        Entry(frame, textvariable=self.red_var, justify='right').grid(row=1, column=2)
        Entry(frame, textvariable=self.green_var, justify='right').grid(row=2, column=2)
        Entry(frame, textvariable=self.blue_var, justify='right').grid(row=3, column=2)

        self.canvas = Canvas(win, bg="grey70", width=300, height=200)
        self.canvas.pack()
        self.oval = self.canvas.create_oval(10, 10, 290, 190, fill="white", width=3) 
        color = "#%02x%02x%02x"%(self.red, self.green, self.blue)
        self.canvas.itemconfig(self.oval, fill=color)  

    def changeRed(self, duty): 
        global RED
        self.red = int(RED)
        self.red_var.set(int(RED))
        color = "#%02x%02x%02x"%(self.red, self.green, self.blue) 
        self.canvas.itemconfig(self.oval, fill=color)

    def changeGreen(self, duty): 
        global GREEN
        self.green = int(GREEN)
        self.green_var.set(int(GREEN))
        color = "#%02x%02x%02x"%(self.red, self.green, self.blue) 
        self.canvas.itemconfig(self.oval, fill=color)

    def changeBlue(self, duty): 
        global BLUE
        self.blue = int(BLUE)
        self.blue_var.set(int(BLUE))
        color = "#%02x%02x%02x"%(self.red, self.green, self.blue) 
        self.canvas.itemconfig(self.oval, fill=color)

def main():
    count=0
    while True:
        if count==0:
            webRemoteControlServer.run(host="172.30.1.14", port=8080, debug=False)
            count+=1
        else:
            time.sleep(1)

def run_rc_drawing():
    count=0
    global app
    while True:
        if count==0:
            window = Tk()
            window.geometry("400x400")
            window.wm_title('Color Selection Sliders') 
            app = RemoteControl_Drawing(window)
            window.mainloop()
            count+=1
        else:
            time.sleep(1)

t1=Thread(target = main, args=()).start()
t2=Thread(target = run_rc_drawing, args = ()).start()
while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        break
 
