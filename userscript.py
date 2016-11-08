import os                   #LINUX FUNCTIES
import sys                  #SYS FUNCTIES
import time                 #TIJD FUNCTIES
import RPi.GPIO as GPIO     #GPIO FUNCTIE
import getpass              #Password module
import os                   #LINUX FUNCTIES
import sys                  #SYS FUNCTIES
import time                 #TIJD FUNCTIES
import RPi.GPIO as GPIO     #GPIO FUNCTIE
import getpass              #Password module
import picamera             #Camera module
from time import sleep      #Voor camera module
GPIO.setmode(GPIO.BCM)      #GPIO NUMMERS (BOARD = PIN NUMMERS)
GPIO.setwarnings(False)     #GEEN WARNINGS
GPIO.setup(17,GPIO.OUT)     #RODE LAMP 1
GPIO.setup(27,GPIO.OUT)     #RODE LAMP 2
GPIO.setup(18,1)            #BUZZER ALARM
GPIO.setup(25, GPIO.IN)     #BUTTON 3
GPIO.setup(4,GPIO.IN)       #MOTION SENSOR BCM
GPIO.setup(23,GPIO.OUT)     #2 GROENE LED'S
GPIO.output(23,GPIO.HIGH)   #2 GROENE LED'S
GPIO.setup(24, GPIO.IN)     #KNOP 1
GPIO.setup(22, GPIO.IN)     #KNOP 2

while True: # SCRIPT VOOR DE BUTTONS .1 START --> GAAT DOOR NAAR LOGIN SCRIPT
    if ( GPIO.input(24) == False ): # Als knop 1 wordt ingedrukt (False) start het script. Hij "breakt" naar lijn 99.
        print ("(----------------------------------------)")
        print("--KNOP INGEDRUKT")
        print ("(----------------------------------------)")
        print ("")
        GPIO.output(23,0)
        time.sleep(.24)
        GPIO.output(23,1)
        time.sleep(.24)
        time.sleep(2)
        break
    if ( GPIO.input(22) == False ): # Als knop 2 wordt ingedrukt stopt het hele script.
        print ("(----------------------------------------)")
        print("--SYSTEEM UITGESCHAKELD \n--FIJNE DAG VERDER!")
        print ("(----------------------------------------)")
        GPIO.output(23,0)
        time.sleep(.22)
        GPIO.output(23,1)
        time.sleep(.22)
        time.sleep(2)
        GPIO.cleanup()
        sys.exit()
    else: # Dit wordt als eerste geactiveerd. Je moet dan knop 1 of knop 2 indrukken.
        os.system('clear')
        print ("(--------------------------------------------------------------)")
        print ("--DRUK OP DE AAN KNOP OM HET SYSTEEM TE STARTEN.")
        print ("--OF DRUK OP DE EXIT KNOP OM HET ALARM SYSTEEM UIT TE SCHAKELEN.")
        print ("(--------------------------------------------------------------)")
        os.system ("date")
        time.sleep(1)


def login(): # LOGIN SCRIPT
    try: #Hier wordt de user gevraagd om username en password.
        print ("(---------------------------------------------)")
        print("--WELKOM BIJ SECURITY SYSTEM ROOKWORST 2.0 \n--LOGIN OM TOEGANG TE KRIJGEN TOT UW SYSTEEM:!")
        print ("(---------------------------------------------)")
        username = raw_input("Voer uw gebruikersnaam in:")
        password = getpass.getpass("Voer je wachtwoord in:")
        usernamedata = open('username.txt', 'r') # Het bestand met de username wordt geopend.
        passwordata = open('password.txt', 'r') # Het bestand met het wachtwoord wordt geopend.
        check1 = usernamedata.read()
        check2 = passwordata.read()

        if username == str(check1) and password == str(check2): # Hier wordt de ingevulde username en password met de database vergeleken.
            print ("")                                          # Als dit klopt gaat uw verder in het programma.
            print ("(----------------------------------------)")
            print ("Login Succesfully! Welcome " + usernamedata.read())
            print ("(----------------------------------------)")
            usernamedata.close()
            passwordata.close()
        else:
            print ("Sorry de gegevens zijn incorrect... Tot ziens!") #Als de gegevens niet correct zijn stopt het script volledig.
            time.sleep(8)
            GPIO.cleanup()
            sys.exit(0)
    except (GPIO.input(22) == False): # Als knop 2 wordt ingedrukt stopt het script. Ook als het script hierboven vastloopt wordt de error opgevangen.
            print ("(----------------------------------------)")
            print("--SYSTEEM UITGESCHAKELD \n--FIJNE DAG VERDER!")
            print ("(----------------------------------------)")
            GPIO.output(22,0)
            time.sleep(.23)
            GPIO.output(22,1)
            time.sleep(.23)
            time.sleep(2)
            GPIO.cleanup()
            sys.exit(1)
    except KeyboardInterrupt: # Als je interrupt word de error opgevangen.
            print ("\n terminated by user")
            GPIO.cleanup()
            sys.exit()
login() # Hier wordt het login script uitgevoerd.
try:
	while True: #Als je succesvol bent ingelogd ga je automatisch hier heen voor het keuze menu.
	    while True:
			try:
				KEUZE = 0
				count = 0
				print ("")
				print ("WAT WIL JE GAAN DOEN? KIES UIT HET VOLGENDE:")
				print ("")
				print ("-->1. DE RODE LAMPJES LATEN KNIPPEREN")
				print ("-->2. DE GROENE LAMPJES LATEN KNIPPEREN")
				print ("-->3. DE GROENE & RODE LAMPJES LATEN KNIPPEREN")
				print ("-->4. LICHTSENSOR")
				print ("-->5. ALARM TESTEN")
				print ("-->6. MOTION DETECTION STARTEN")
				print ("-->7. SYSTEEM UITSCHAKELEN")
				print ("-->8. MINI-PROJECT CIJFER BEREKENEN")
				print ("-->9. ALARM SYSTEEM EXTRA VAGANZA")
				print ("-->10. WACHTWOORD WIJZIGEN")
				print ("-->11. 5 FOTO'S MAKEN.")
				print ("-->12. VIDEO MAKEN.")
				print ("-->13. REACTIESPEL STARTEN.")
				print ("")
				KEUZE = input("MAAK EEN KEUZE UIT: 1, 2, 3 , 4, 5, 6, 7, 8, 9, 10, 11, 12, 13: ")
				print ("")
				KEUZE = int(KEUZE)
			except ValueError:
				print("Invoer moet een integer zijn! Probeer opnieuw.")
				continue
			except NameError:
				print("Invoer moet een integer zijn! Probeer opnieuw.")
				continue
			except TypeError:
				print("Invoer moet een integer zijn! Probeer opnieuw.")
				continue
			except SyntaxError:
				print ("Invoer moet een integer zijn! Probeer opnieuw.")
				continue 
			if KEUZE > 0 and KEUZE < 14:
				break
			else:
				print("Onjuiste invoer! Probeer opnieuw.")
	    if KEUZE == "":
		    print("GEEN INVOER! Probeer opnieuw!")
		    continue
	    if KEUZE == 1: # Bij keuze 1 wordt de user gevraagd hoe vaak je het rode lampje wil laten knipperen. Daarna wordt het uitgevoerd.
		    os.system('clear')
		    print ("")
		    print ("JE KOOS VOOR DE OPTIE: RODE LAMPJES LATEN KNIPPEREN.")
		    count = input("HOE VAAK WIL JE HET LATEN KNIPPEREN? ")
		    while count > 0:
		            GPIO.output(27,GPIO.HIGH)
		            GPIO.output(17,GPIO.HIGH)
		            time.sleep(1)
		            GPIO.output(27,GPIO.LOW)
		            GPIO.output(17,GPIO.LOW)
		            time.sleep(1)
		            count = count - 1
		    continue
	    if KEUZE == 2: # Bij keuze 2 wordt de user gevraagd hoe vaak je het groene lampje wil laten knipperen. Daarna wordt het uitgevoerd.
		    os.system('clear')
		    print ("")
		    print ("JE KOOS VOOR DE OPTIE: GROENE LAMPJES LATEN KNIPPEREN.")
		    count = input("HOE VAAK WIL JE HET LATEN KNIPPEREN? ")
		    while count > 0:
		            GPIO.output(23,GPIO.HIGH)
		            time.sleep(1)
		            GPIO.output(23,GPIO.LOW)
		            time.sleep(1)
		            count = count - 1
	    if KEUZE == 3: # Bij keuze 3 wordt de user gevraagd hoe vaak je het rode en groene lampje wil laten knipperen. Daarna wordt het uitgevoerd.
		    os.system('clear')
		    print ("DE GROENE & RODE LAMPJES LATEN KNIPPEREN.")
		    count = input("HOE VAAK WIL JE HET LATEN KNIPPEREN? ")
		    while count > 0:
		        GPIO.output(27,GPIO.HIGH)
		        GPIO.output(17,GPIO.HIGH)
		        GPIO.output(23,GPIO.HIGH)
		        time.sleep(1)
		        GPIO.output(27,GPIO.LOW)
		        GPIO.output(17,GPIO.LOW)
		        GPIO.output(23,GPIO.LOW)
		        time.sleep(1)
		        count = count - 1
	    if KEUZE == 4: # De lichtsensor die aan de pi vast zit meet het licht. Dit wordt via een extern script gedaan.
		    os.system("clear")
		    print ("(-----------------------------------)")
		    print ("JE KOOS VOOR DE OPTIE: LICHTSENSOR")
		    print ("(-----------------------------------)")
		    print ("--LICHTSENSOR WORDT GESTART \n--LAGE VALUE GEEFT AAN DAT ER VEEL LICHT IS.\n--HOGE VALUE GEEFT VEEL LICHT")
		    os.system("sudo python /home/pi/ldr2.py")
	    if KEUZE == 5: # Hier kan je kijken of het alarm systeem werkt. De user wordt gevraagd hoe vaak je het alarm wil laten afgaan.
		    os.system('clear')
		    print ("JE KOOS VOOR DE OPTIE: ALARMSYSTEEM TESTEN.")
		    print ("(-------------------------------------------------------)")
		    print ("SOMEONE IS BREAKING IN!!!")
		    print ("(-------------------------------------------------------)")
		    os.system("sudo python /home/pi/Project-CSN/alarmpro.py")
		        
	    if KEUZE == 6: # Hier wordt het alarm systeem gestart met motion sensor. Hier wordt ook naar een extern script verwezen.
		    os.system('clear') # Dit maakt het scherm tekst vrij zodat je het overzichtelijk kan lezen mocht het alarm af gaan.
		    print ("JE KOOS VOOR DE OPTIE: MOTION SENSOR STARTEN.")
		    print ("MOTION SENSOR IS NOW ACTIVE !!!")
		    os.system ("date")
		    def motion_detect():
		        try:
		            while True:
		                if GPIO.input(4) == 1:
		                    os.system ("sudo python /home/pi/Project-CSN/alarmpro.py")
		        except KeyboardInterrupt:
		            print ("(---------------------------------------------)")
		            print ("--SYSTEEM UITGESCHAKELD \n--FIJNE DAG VERDER!")
		            print ("(---------------------------------------------)") 
			    GPIO.cleanup()
		            sys.exit()
		    if __name__ == "__main__":
		        motion_detect()
	    if KEUZE == 7: # Hiermee sluit je het systeem netjes af. De GPIO's worden schoon gemaakt en het script word afgesloten.
		    os.system("clear")
		    print ("JE KOOS VOOR DE OPTIE: SYSTEEM UITSCHAKELEN")
		    print ("(----------------------------------------)")
		    print ("--SYSTEEM UITGESCHAKELD \n--FIJNE DAG VERDER!")
		    print ("(----------------------------------------)")
		    GPIO.cleanup()
		    sys.exit()
	    if KEUZE == 8: # Complete onzin die we grappig vonden om toe te voegen.
		    os.system("clear")
		    print ("JE KOOS VOOR DE OPTIE: MINI-PROJECT CIJFER BEREKENEN")
		    print ("(--------------------------------------------------------)")
		    print ("c^2*2,353*0 ^(-8)+h*e^(-5c*t)=1,3583*11^(-5)= 10+")
		    print ("(--------------------------------------------------------)")
		    print ("-- OVER 15 SECONDEN STOPT HET SCRIPT")
		    time.sleep(15)
	    if KEUZE == 9: # het alarmsysteem die nog niet perfect werkt. Het was lastig om de camera, motionsensor, alarm systeem en muziek af te spelen te combineren
			keuze = input("VOOR ALARM SYSTEEM PRO +. KIES 1") # Het werkt wel bijna perfect maar er lopen nog sommige dingen vast waar we niet genoeg tijd voor hadden
			if keuze == 1:                                     # In linux werkt bijvoorbeeld muziek afspelen anders dan op windows.
				os.system('clear')
				print ("WELKOM BIJ ALARMSYSTEEM PRO.")
				os.system ("date")
				def motion_detect():
						while True:
							if GPIO.input(4) == 1:
								os.system("sudo python /home/pi/Project-CSN/alarmproextra.py")
				motion_detect()
	    if KEUZE == 10: # Username en wachtwoord wijzigen
			print ("JE KOOS VOOR DE OPTIE: USERNAME & WACHTWOORD WIJZIGEN")
			print ("")
			if GPIO.input(24) == True:
				nieuwe_username = raw_input('Voer uw nieuwe gebruikersnaam in: ') # Nieuwe username
				nieuw_wachtwoord = raw_input('Voer uw nieuwe wachtwoord in: ') # Nieuw wachtwoord
				wachtwoord_gelijk = raw_input('Voer uw nieuwe wachtwoord nog een keer in: ') #controle wachtwoord
				if nieuw_wachtwoord == wachtwoord_gelijk: # Hier wordt gekeken of je 2x hetzelfde wachtwoord hebt ingetypt.
					username = open('username.txt', 'w') # username data wordt geopend en leeg gemaakt
					password = open('password.txt', 'w') # password data wordt geopend en leeg gemaakt
					username.write(nieuwe_username) # De nieuwe username wordt nu in het bestand geschreven
					password.write(wachtwoord_gelijk) # Het nieuwe wachtwoord wordt geschreven naar het bestand.
					print("Bedankt voor het wijzigen. Het systeem word nu afgesloten.")
					username.close()
					password.close()
					GPIO.cleanup()
					sys.exit() # Alles wordt afgesloten en nu heb je nieuwe inlog gegevens.
				else:
					print("Wachtwoord is niet gewijzigd.") # Mocht je bijvoorbeeld 2 verschillende wachtwoorden hebben ingetypt.
					continue
			else:
				continue

	    if KEUZE == 11: # Een optie om met de camera een foto te maken
			os.system("clear")
			print ("JE KOOS VOOR DE OPTIE: FOTO MAKEN")
			print ("ER WORDEN 5 FOTO'S GEMAAKT \nCHECK JE DOCUMENTEN OM DE FOTO'S TE BEKIJKEN.")
			print ("(----------------------------------------)")
			camera = picamera.PiCamera() # Hier wordt de geimporteerde module leesbaar gemaakt voor python.
			camera.resolution = (2592, 1944) #resolutie en andere gegevens worden hieronder gezet zodat er een mooi resultaat is.
			camera.brightness = 70
			camera.sharpness = 0
			camera.contrast = 20
			camera.brightness = 50
			camera.saturation = 0
			camera.ISO = 0
			camera.video_stabilization = False
			camera.exposure_compensation = 0
			camera.exposure_mode = 'auto'
			camera.meter_mode = 'average'
			camera.awb_mode = 'auto'
			camera.image_effect = 'none'
			camera.color_effects = None
			camera.rotation = 0
			camera.hflip = False
			camera.vflip = False
			camera.crop = (0.0, 0.0, 1.0, 1.0)
			camera.capture('image1.jpg') # Foto's worden gemaakt om de 2 seconden en opgeslagen als ImageX.jpg in mijn documenten.
			print("Foto 1 is gemaakt. Nog 4 te gaan.")
			sleep(2)
			camera.capture('image2.jpg')
			print("Foto 2 is gemaakt. Nog 3 te gaan.")
			sleep (2)
			camera.capture("image3.jpg")
			print("Foto 3 is gemaakt. Nog 2 te gaan.")
			sleep (2)
			camera.capture('image4.jpg')
			print("Foto 4 is gemaakt. Nog 1 te gaan.")
			sleep (2)
			camera.capture("image5.jpg")
			print("Foto 5 is gemaakt. Dit was de laatste.")
			print("Check je documenten om de foto's te zien!")
			GPIO.cleanup()
			sys.exit()

	    if KEUZE == 12: # Hier wordt een klein filmpje gemaakt met de camera
			os.system("clear")
			print ("JE KOOS VOOR DE OPTIE: VIDEO MAKEN")
			print ("ER WORDT EEN VIDEO GEMAAKT \nCHECK JE DOCUMENTEN OM DE VIDEO TE BEKIJKEN.")
			print ("(----------------------------------------)")
			camera = picamera.PiCamera() # Camera wordt leesbaar gemaakt voor python
			camera.resolution = (1920, 1080) #resolutie en andere gegevens worden bepaald.
			camera.brightness = 70
			camera.sharpness = 0
			camera.contrast = 30
			camera.brightness = 50
			camera.saturation = 0
			camera.ISO = 0
			camera.video_stabilization = False
			camera.exposure_compensation = 0
			camera.exposure_mode = 'auto'
			camera.meter_mode = 'average'
			camera.awb_mode = 'auto'
			camera.image_effect = 'none'
			camera.color_effects = None
			camera.rotation = 0
			camera.hflip = False
			camera.vflip = False
			camera.crop = (0.0, 0.0, 1.0, 1.0)
			camera.start_recording('video1.h264') # Zo heet het filmpje die wordt opgeslagen in mijn documenten
			sleep(5)
			camera.stop_recording()
			GPIO.cleanup()
			sys.exit()
            if KEUZE == 13:
			os.system("clear")
			print ("JE KOOS VOOR DE OPTIE: REACTIE SPEL STARTEN")
			os.system ("date")
			os.system ("sudo python /home/pi/Project-CSN/reaction.py")
			os.system ("clear")

	   # if KEUZE == 13: # Het alarm systeem met motion sensor. Als de sensor af gaat worden er 4 fotos gemaakt. Zo kan je de dader zien.
	#		os.system('clear')
	#		print ("JE KOOS VOOR DE OPTIE: MOTION SENSOR + CAMERA.")
	#		os.system ("date")
	#		def motion_detect(): # alarm systeem script wordt opgeroepen.
	#			try:
	#				while True:
	#					if GPIO.input(4) == 1:
	#						os.system ("sudo python /home/pi/Project-CSN/alarmpro2.py")
	#			except (GPIO.input(22) == False):
	#				print ("(---------------------------------------------)")
	#				print ("--SYSTEEM UITGESCHAKELD \n--FIJNE DAG VERDER!")
	#				print ("(---------------------------------------------)")
	#				GPIO.output(22,0)
	#				time.sleep(.23)
	#				GPIO.output(22,1)
	#				time.sleep(.23)
	#				time.sleep(2)
	#				GPIO.cleanup()
	#				sys.exit()
	#		if __name__ == "__main__":
	#			motion_detect() #motion sensor script wordt opgeroepen.
except KeyboardInterrupt: # Als je interrupt word de error opgevangen.
            print ("\n TERMINATED BY USER...GOODBYE")
            GPIO.cleanup()
            sys.exit()

