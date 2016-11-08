import sys
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD) # LET OP DIT IS BOARD GEEN BCM --> BOARD PIN NUMMER.
pin_to_circuit = 5
def rc_time (pin_to_circuit):
    count = 0
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.6)
    GPIO.setup(pin_to_circuit, GPIO.IN)
   	#Tel tot de ping omhoog gaat.
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1
    return (count, "<--- LICHTWAARDE")

#Script interrupted met cleanup.
try:
    # Main loop
    while True:
        print rc_time(pin_to_circuit)
except KeyboardInterrupt:
    print ("\n TERMINATED BY USER... GOODBYE!")
    GPIO.cleanup()
    sys.exit(1)

