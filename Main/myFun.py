import time
import datetime
import os

def getTimeCap():
    now = time.localtime()
    nowTime = datetime.datetime.now().strftime("%d-%H:%M:%S")
    nowTime = nowTime + ".png"
    return nowTime

def getTimeREC():
    now = time.localtime()
    nowTime = datetime.datetime.now().strftime("%d-%H:%M:%S")
    nowTime = nowTime + ".wav"
    return nowTime    


def getDay():
    return datetime.datetime.now().strftime("%Y-%m-%d")

def getTime():
    return datetime.datetime.now().strftime("%H:%M")

def getData():
    f = open("./result.txt", 'r')
    result_data = f.readline()
    f.close
    return result_data

def myRemove(filename):
    os.remove(filename)