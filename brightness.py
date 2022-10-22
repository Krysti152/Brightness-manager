#!/usr/bin/python3
import os




act_val = 0.
max_val = 16.
min_val = 2.
steps = 7
act_step = 0
n = (max_val - min_val) / (steps-1)


def read_val(path="/home/krystian/skrypty/.brightness.txt"):
    global act_val
    global act_step
    with open(path,"r") as file:
        l = file.readlines()
        act_val = float(l[0].replace("\n", '')) * 10
        act_step = int(l[1].replace("\n",""))

def notify_send(msg):
    os.system("notify-send -t 200 'Janość Ekranu' '" + msg + "'.")

def set_brightness(__val):
    os.system("xrandr --output LVDS1 --brightness " + str(__val))

def save():
    global act_step
    os.system("/home/krystian/skrypty/save_bright.sh")
    os.system("echo " + str(act_step) + " >> /home/krystian/skrypty/.brightness.txt")


def sub():
    global steps
    global act_step
    global n
    global min_val
    if act_step > 0:
        act_step -= 1
        notify_send("Ustawiono na " + str(act_step))
    set_brightness((n * act_step + min_val) / 10)
    save()


def add():
    global steps
    global act_step
    global act_val
    global n
    global min_val
    if act_step < steps-1:
        act_step += 1
        notify_send("Ustawiono na " + str(act_step))
    set_brightness((n * act_step + min_val) / 10)
    save()


read_val()
