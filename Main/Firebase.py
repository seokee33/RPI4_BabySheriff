from pyfcm import FCMNotification
import GPIOControll as gp
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


APIKEY = "??"
 
TOKEN = "??"

#firebase
cred = credentials.Certificate("babaysheriff-firebase-adminsdk-g1hpu-e27a3946fe.json")

firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://babaysheriff-default-rtdb.firebaseio.com/'
})


# 파이어베이스 콘솔에서 얻어 온 서버 키를 넣어 줌
push_service = FCMNotification(APIKEY)
 
def sendMessage(body, title):
    
    # 메시지 (data 타입)
    data_message = {
        "body": body,
        "title": title
    }
    
    # 토큰값을 이용해 1명에게 푸시알림을 전송함
    result = push_service.single_device_data_message(registration_id=TOKEN, data_message=data_message)
    jsonValue = str(result)
    jsonArr = jsonValue.split(',')
    if jsonArr[1].find("1") == -1:
        print(jsonArr[1])
        gp.allOFF()
        gp.turnRed()
    else:
        gp.allOFF()
        gp.turnGreen()

    # 전송 결과 출력
    print(result)




def insertTemp(nowDate, nowDateTime, targetTemp):
    dir = db.reference('Temp/'+nowDate)
    dir.update({nowDateTime : targetTemp})
