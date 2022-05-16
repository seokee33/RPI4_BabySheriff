import cv2
import pyaudio
import wave


def capture(imgName):
    camid = 0
    # 윈도우 사용자는 마지막에 cv2.CAP_DSHOW 추가
    # 우분투에선 cam = cv2.VideoCapture(camid)
    cam = cv2.VideoCapture(camid, cv2.CAP_DSHOW)
    
    if cam.isOpened() == False:
        print ('cant open the cam (%d)' % camid)
        return None

    ret, frame = cam.read()
    if frame is None:
        print ('frame is not exist')
        return None
    
    # png로 저장 
    cv2.imwrite(imgName,frame, params=[cv2.IMWRITE_PNG_COMPRESSION,0])
    cam.release()



#Audio
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 20

def recordAudio(test_img_name):
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                 channels=CHANNELS,
                 rate=RATE,
                 input=True,
                 frames_per_buffer=CHUNK)
    print("Start to record the audio.")
    frames = []
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
      data = stream.read(CHUNK)
      frames.append(data)
    print("Recording is finished.")
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(test_img_name, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()