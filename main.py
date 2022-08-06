### TODO
# - Aggiungere main - DONE
# - Spostare gestione log in una funzione apposita - DONE
# - Aggiungere init per inizializzare variabili file ecc
# - aggiungere gestione dell'uscita (CTRL+C), ricordarsi di chiudere il file - DONE
# - ottimizzazioni varie (dove possibile)

import os
import sys
import logging
from time import sleep
from datetime import datetime
from gpiozero import DistanceSensor

os.system('vcgencmd display_power 0 > /dev/null 2>&1')
ultrasonic = DistanceSensor(echo=17, trigger=4, max_distance=4, threshold_distance=3)
logging.basicConfig(filename='projector.log', encoding='utf-8', level=logging.DEBUG)

def main(argv=None):
    cnt = 0
    try:
        while True:
            os.system('clear')
            ultrasonic.wait_for_in_range()

            cnt +=1
            curDT = datetime.now()
            logging.info('\nDate: ' + curDT.strftime("%m/%d/%Y, %H:%M:%S") + ' - Cnt: ' + str(cnt) + '\n')

            os.system('vcgencmd display_power 1 > /dev/null 2>&1')
            os.system('cvlc video/Naruto.mp4 --play-and-exit --quiet > /dev/null 2>&1')
            os.system('vcgencmd display_power 0 > /dev/null 2>&1')
            sleep(2)
    except KeyboardInterrupt:
        os.system('killall cvlc')
        os.system('vcgencmd display_power 1 > /dev/null 2>&1')

if __name__ == '__main__':
    sys.exit(main())
