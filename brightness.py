#!/usr/bin/python3
import os




def_path = "/home/$USER/brightness-manager/"
max_val = 16.
min_val = 2.
steps = 7




act_step = 0
act_val = 0.
n = (max_val - min_val) / (steps-1)


def read_val(path=def_path):
    global act_val
    global act_step
    with open(path+".brightness.txt","r") as file:
        l = file.readlines()
        act_val = float(l[0].replace("\n", '')) * 10
        act_step = int(l[1].replace("\n",""))

def notify_send(msg):
    os.system("notify-send -t 200 'Janość Ekranu' '" + msg + "'.")

def set_brightness(__val):
    os.system("xrandr --output LVDS1 --brightness " + str(__val))

def save():
    global act_step
    global def_path
    os.system(def_path + "save_bright.sh")
    os.system("echo " + str(act_step) + " >> "+def_path+".brightness.txt")


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
