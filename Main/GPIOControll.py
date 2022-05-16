import RPi.GPIO as GPIO
import board
import busio as io
import adafruit_mlx90614

GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT) #red
GPIO.setup(20,GPIO.OUT) #green
GPIO.setup(21,GPIO.OUT) #blue

def allOFF():
    GPIO.output(16,False)
    GPIO.output(20,False)
    GPIO.output(21,False)

def turnRed():
    allOFF()
    GPIO.output(16,True)
    GPIO.output(20,False)
    GPIO.output(21,False)
    
def turnGreen():
    allOFF()
    GPIO.output(20,True)
    GPIO.output(16,False)
    GPIO.output(21,False)

def turnBlue():
    allOFF()
    GPIO.output(21,True)
    GPIO.output(16,False)
    GPIO.output(21,False)    

#체온
i2c = io.I2C(board.SCL, board.SDA, frequency=100000)
mlx = adafruit_mlx90614.MLX90614(i2c)

def getTemp():
    temp = "{:.2f}".format(mlx.object_temperature)
    return temp
    
