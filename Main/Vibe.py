import requests
import os
import GPIOControll as gp
ip = "192.168.43.117/gpio/1"
def vibe():
    try:
        r = requests.get(ip) #url주소에 데이터 요청 
        webbrowser.open(ip);
        os.system("pkill " +"chromium");
        gp.allOFF()
        gp.turnGreen()
    except requests.exceptions.ConnectionError as errc:
        gp.allOFF()
        gp.turnBlue()
        print("Error Connecting : ", errc)
        print("오류입니다.")