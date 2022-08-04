# motion-projector-activator

## Set-up

Viste le ridotte risorse hw presenti sul Raspi Zero W (v 1) si è deciso di installare la versione del S.O. senza GUI.

Dopo aver avviato il raspi, la prima operazione preliminare è quella di installare vlc.
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install vlc
```

Per poter avviare correttamente lo script dopo il boot ed il login utente all'accensione del dispositivo, è necessario aggiungerlo al file .bashrc
```
sudo nano /home/pi/.bashrc
sudo python /home/pi/sample.py
```

ref. [Qui](https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/)

Siccome lo script all'avvio verrà avviato come root e vlc di default non può essere avviato da quest'utente, bisogna cambiare l'user che chiama il processo:
sudo sed -i 's/geteuid/getppid/' /usr/bin/vlc

ref. [Qui](https://www.tecmint.com/run-vlc-media-player-as-root-in-linux/)

<br><br>

## Link utili

VLC command-line --> https://wiki.videolan.org/VLC_command-line_help/
Raspberry pi foundation official tutorial ultrasonic sensor --> https://projects.raspberrypi.org/en/projects/physical-computing/12
