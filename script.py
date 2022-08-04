from time import sleep
import os
from gpiozero import DistanceSensor
import logging
from datetime import datetime

ultrasonic = DistanceSensor(echo=17, trigger=4, max_distance=4, threshold_distance=3)
os.system('vcgencmd display_power 0 > /dev/null 2>&1')
f = open("log.txt", "a")
cnt = 0
while True:
    os.system('clear')
    ultrasonic.wait_for_in_range()

    cnt +=1
    curDT = datetime.now()
    f.write('\nDate: ' + curDT.strftime("%m/%d/%Y, %H:%M:%S") + ' - Cnt: ' + str(cnt) + '\n')

#os.system('sudo killall vlc')
    os.system('vcgencmd display_power 1 > /dev/null 2>&1')
    os.system('cvlc Naruto.mp4 --play-and-exit --quiet > /dev/null 2>&1')
    #os.system('mplayer -vo xv Naruto.mp4')
    os.system('vcgencmd display_power 0 > /dev/null 2>&1')
    sleep(2)
    
    
    ### TODO
    # - Aggiungere main
    # - Spostare gestione log in una funzione apposita
    # - Aggiungere init per inizializzare variabili file ecc
    # - aggiungere gestione dell'uscita (CTRL+C), ricordarsi di chiudere il file
    # - varie
