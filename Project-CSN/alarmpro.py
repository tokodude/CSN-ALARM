import sys
import time # libarry voor de tijd die aan en uit gaat.
import RPi.GPIO as GPIO # standaard GPIO import
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setwarnings(False)
GPIO.setup(25, GPIO.IN)
GPIO.setup(22, GPIO.IN)

count = 0
try:
    while 1 and count <= 5:
        print ("(-------------------------------------------------------)")
        print ("MOTION DETECTION TRIGGERD!!! SOME ONE IS BREAKING IN!!!")
        print ("(-------------------------------------------------------)")
        GPIO.output(17,GPIO.HIGH)
        GPIO.output(27,GPIO.HIGH)
        time.sleep(1)
        GPIO.output(17,GPIO.LOW)
        GPIO.output(27,GPIO.LOW)
        time.sleep(1)
        GPIO.output(18,0)
        time.sleep(0.7)
        GPIO.output(18,1)
        time.sleep(0.7)
        print ("ALARM IS SET INTACTIVE IN 10 SECONDS")
        count = count + 1
        if (GPIO.input(25) == False ):
            print ("(----------------------------------------)")
            print("--ALARM UITGESCHAKELD")
            print ("(----------------------------------------)")
            time.sleep(5)
            GPIO.cleanup()
            sys.exit()
        if ( GPIO.input(22) == False ):
            print ("(----------------------------------------)")
            print("--ALARM UITGESCHAKELD")
            print ("(----------------------------------------)")
            time.sleep(5)
            GPIO.cleanup()
            sys.exit()
except KeyboardInterrupt:
    print ("\n TERMINATED BY USER... GOODBYE!")
    GPIO.cleanup()
    sys.exit(1)

