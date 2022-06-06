import numpy as np
import os
import librosa
from keras.models import Sequential
from keras.models import model_from_json
import Firebase as fcm

def preprocess(filename):
    y,sr=librosa.load(filename)
    mfccs = np.mean(librosa.feature.mfcc(y, sr, n_mfcc=36).T,axis=0)
    melspectrogram = np.mean(librosa.feature.melspectrogram(y=y, sr=sr, n_mels=36,fmax=8000).T,axis=0)
    chroma_stft=np.mean(librosa.feature.chroma_stft(y=y, sr=sr,n_chroma=36).T,axis=0)
    chroma_cq = np.mean(librosa.feature.chroma_cqt(y=y, sr=sr,n_chroma=36).T,axis=0)
    chroma_cens = np.mean(librosa.feature.chroma_cens(y=y, sr=sr,n_chroma=36).T,axis=0)
    features=np.reshape(np.vstack((mfccs,melspectrogram,chroma_stft,chroma_cq,chroma_cens)),(36,5))
    return(features)

def cry2(filename):
    json_file = open('./model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights("./model.h5")
    loaded_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    print("Loaded model from disk")

    file = preprocess(filename)
    file=np.reshape(file,(1,36,5,1))
    result = np.argmax(loaded_model.predict(file), axis=-1)
    print("result : ", result)
    print("0: awake , 1: diaper , 2: hungry , 3: sleepy")

    from datetime import datetime

    current_time = datetime.now()

    if result == [0]:
        print("[",current_time,"] result : 일어남")
        fcm.sendMessage("울음감지","현재 : 일어남")
    elif result == [1]:
        print("[",current_time,"] result : 기저귀")
        fcm.sendMessage("울음감지","현재 : 기저귀")
    elif result == [2]:
        print("[",current_time,"] result : 배고픔")
        fcm.sendMessage("울음감지","현재 : 배고픔")
    elif result == [3]:
        print("[",current_time,"] result : 졸림")
        fcm.sendMessage("울음감지","현재 : 졸림")

def cry1(filename):
    json_file = open('./model_1.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights("./model_1.h5")
    loaded_model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    print("Loaded model from disk")

    file = preprocess(filename)
    file=np.reshape(file,(1,36,5,1))
    result = np.argmax(loaded_model.predict(file), axis=-1)
    print("result : ", result)
    print("0: babycry, 1: Noise ")
    
    
    #print("0: babycry1 , 1: babycry2 , 2: Noise ")

    from datetime import datetime

    current_time = datetime.now()

    if result == [0]:
        print("[",current_time,"] result : cry")
        cry2(filename)
    elif result == [1]:
        print("[",current_time,"] result : cry")
        cry2(filename)






