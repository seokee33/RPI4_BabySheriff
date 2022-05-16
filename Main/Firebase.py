from pyfcm import FCMNotification
import GPIOControll as gp
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


APIKEY = "AAAASAX4W9c:APA91bE5VC1dGpXud_tr2WoAHuBmde7UY-OVFqHeBDacjAvVeZFK5Imj5uTBJakJ_-D2tAvYALn4qid3BVF0Y_1udW1ooKFBI0rAXVUC4_tAuFe4dJN7C1vJcI3HOqeystTDmaIUkRjR"
 
TOKEN = "fkUXBcHVQWyA0ozykQRPyR:APA91bG2EeKF1Z_hTS4TWf6yyfawe5E1U3o0RhzQBV2LVcMweDJeQiiQR5kbOVd5Q9gV6egnzkgk8ZZ2sWPtc5cmqvGOp_vzzT_l6r_Y0Bfc9_2IvMETrrbJw9ZZBpy8hpWV9rHD5FPD"

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