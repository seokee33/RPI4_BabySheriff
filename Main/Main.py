import CamRec as CR
import GPIOControll as contoller
import os
import subprocess
import Firebase as firebase
import RPi.GPIO as GPIO
import board
import busio as io
import Vibe as vibe
import myFun as my
import time
import cry

#AUDIO
soundpin = 17
GPIO.setup(soundpin,GPIO.IN)

def camProg():
    send_result = ""
    capName = my.getTimeCap()
    CR.capture(capName)
    subprocess.call("python3 ~/Main/yolov5/detect.py --source ./"+capName + " --weights ./runs/train/exp/weights/best.pt --conf 0.25", shell=True)
    result_data = my.getData()
    my.myRemove(capName)
    print(result_data)
    if(result_data != "baby"):
        count = 0
        for i in range(2):
            capName = my.getTimeCap()
            CR.capture(capName)                    
            subprocess.call("python3 ~/Main/yolov5/detect.py --source ./"+capName + " --weights ./runs/train/exp/weights/best.pt --conf 0.25", shell=True)
            result_data_check = my.getData()
            my.myRemove(capName)
            if(result_data_check != "baby"):
                count += 1
            else:
                break
        if(count == 2):
            send_result = "없음"
            vibe.vibe()
            firebase.sendMessage("cam", "아이가 보이지 않아요")
        else:
            send_result = "존재"
            firebase.insertTemp(my.getDay(),my.getTime(),contoller.getTemp())
    else:
        send_result = "존재"
        firebase.insertTemp(my.getDay(),my.getTime(),contoller.getTemp())
    print("최종 : "+send_result)

if __name__ == "__main__":
    try:
        while(1):
            now = time.localtime()

            if(now.tm_min % 5 == 0):
                camProg()
            
            if GPIO.input(soundpin) == 0:
                print("Sound Dected")
                now_Audio = time.localtime()
                nowTime = my.getTimeREC()
                CR.recordAudio(nowTime)
                try:
                    cry.cry1(nowTime)
                finally:
                    continue

    except KeyboardInterrupt:
        contoller.allOFF()

