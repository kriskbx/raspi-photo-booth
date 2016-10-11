# raspi-photo-booth

> Selfmade thermal printing photobooth featuring raspberry power. &lt;3

![](./PhotoBooth.jpg)

### Hardware used

* 1x [Raspberry PI Model B+](http://amzn.to/2eb9ngF)
* 1x [Raspberry Camera NoIR V2](http://amzn.to/2eb7lx4)
* 1x [Adafruit 60mm Arcade LED Button](http://amzn.to/2dHWpHU)
* 1x [POS58 Thermal Printer](http://amzn.to/2d4lyea)
* 1x [PNP transistor S8550](http://amzn.to/2edacW9)
* 2x [220Ω resistor](http://amzn.to/2dJReXZ)
* 1c [Buzzer 5V (active)](http://amzn.to/2dVzRS1)

### Getting started

```
# Clone the repository
git clone https://github.com/kriskbx/raspi-photo-booth
cd raspi-photo-booth

# Install supervisor
sudo apt-get install supervisord

# Install python requirements
pip install pillow picamera escpos RPi.GPIO

# Add and edit the supervisor-conf to match your paths
cp PhotoBooth.conf /etc/supervisor/conf.d/
vim /etc/supervisor/conf.d/PhotoBooth.conf

# Edit the script to match your GPIO pins and your printer
vim PhotoBooth.py

# Update and start supervisor
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl start photo-booth
```

### Curcuit diagram

![](./curcuit-diagram.png)

### Making of

![](./MakingOf.jpg)

### Contributors

Handwriting by [@johnnieparkstudio](https://www.instagram.com/johnnieparkstudio/)

### License

MIT