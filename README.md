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
sudo python /home/pi/motion-projector-activator/main.py
```

ref. [Qui](https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/)

Siccome lo script all'avvio verrà avviato come root e vlc di default non può essere avviato da quest'utente, bisogna cambiare l'user che chiama il processo:
```
sudo sed -i 's/geteuid/getppid/' /usr/bin/vlc
```

ref. [Qui](https://www.tecmint.com/run-vlc-media-player-as-root-in-linux/)

Alternativamente è possibile avviare vlc con il flag `-wrapper`

altri flag utili sono `--play-and-exit` che serve per uscirer automaticamente dal processo vlc alla fine della riproduzione (altrimenti lo script resterebbe blloccato in attesa di un CTRL+C

e il flag `--quiet` che disattiva tutti i log di warning ed error

Quest'ultimo è opzionale in quanto si è preferito redirigere lo standard output ed error per non "sporcare" la console con i log (di qualunque genere) altrimenti visibili per pochi istanti prima e dopo la riproduzione del video

per fare questo al lancio dei comandi è stata aggiunto `> /dev/null 2>&1` per redirigere appunto l'output della console

ref. [Qui](https://stackoverflow.com/a/33989346)

<br><br>

## Cablaggio

Per il cablaggio si è deciso di utilizzare un cavo ethernet per diversi fattori:
- semplicità nel trovare cavi di lunga dimensione prefabbricati; (5m 3€ su amazon);
- cavo schermato e di buona qualità (cat 6 ecc);
- blocco sulla socket, in modo da prevenire sgancio per strattoni involontari del cavo ecc;
- fino a 8 I/O con un solo cavo passante;

<br><br>

## Link utili

- [VLC command-line](https://wiki.videolan.org/VLC_command-line_help/)
- [Raspberry pi foundation official tutorial ultrasonic sensor](https://projects.raspberrypi.org/en/projects/physical-computing/12)
- [Hide Console When Using os.system](https://thewebdev.info/2022/04/10/how-to-hide-the-console-when-using-os-system-or-subprocess-call-with-python/)
