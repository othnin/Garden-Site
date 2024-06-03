# External module imp
import RPi.GPIO as GPIO
import datetime
import time



GPIO.setmode(GPIO.BOARD) # Broadcom wwpin-numbering scheme
PUMP_PIN = 7
WATER_SENSOR_PIN = 8
WATER_DURATION = 5

def get_last_watered():
    try:
        f = open("../data/last_watered.txt", "r")
        return f.readline()
    except:
        return 0
      
def get_status():
    GPIO.setup(WATER_SENSOR_PIN, GPIO.IN) 
    return GPIO.input(WATER_SENSOR_PIN)

def init_output():
    GPIO.setup(PUMP_PIN, GPIO.OUT)
    GPIO.output(PUMP_PIN, GPIO.LOW)
    GPIO.output(PUMP_PIN, GPIO.HIGH)
    
def auto_water(WATER_DURATION = 5):
    consecutive_water_count = 0
    init_output()
    print("Here we go! Press CTRL+C to exit")
    try:
        while 1 and consecutive_water_count < 10:
            time.sleep(WATER_DURATION)
            wet = get_status()
            if not wet:
                if consecutive_water_count < 5:
                    pump_on()
                consecutive_water_count += 1
            else:
                consecutive_water_count = 0
    except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
        GPIO.cleanup() 

def pump_on(WATER_DURATION = 1):
    init_output()
    f = open("../data/last_watered.txt", "a")
    f.write(format(datetime.datetime.now()) + " " + str(WATER_DURATION)+ '\n')
    f.close()
    GPIO.output(PUMP_PIN, GPIO.LOW)
    time.sleep(WATER_DURATION)
    GPIO.output(PUMP_PIN, GPIO.HIGH)
    

