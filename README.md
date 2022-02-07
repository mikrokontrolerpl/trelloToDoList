# Trello to-do list

This project covers the design of a device that displays a to-do list that is pulled live from a Trello board. The whole is based on the Raspberry Pi Zero 2 WH minicomputer and e-paper display.


## Features

- Display the current list from Trello
- Automatic synchronization
- Screen refresh only when content is changed



## Installation

Install BCM2835 libraries

```bash
wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.60.tar.gz
tar zxvf bcm2835-1.60.tar.gz 
cd bcm2835-1.60/
sudo ./configure
sudo make
sudo make check
sudo make install
```
Install WiringPi libraries

```bash
sudo apt-get install wiringpi
wget https://project-downloads.drogon.net/wiringpi-latest.deb
sudo dpkg -i wiringpi-latest.deb
gpio -v
```    
Install other libraries

```bash
sudo apt-get update
sudo apt-get install python3-pip
sudo apt-get install python3-pil
sudo apt-get install python3-numpy
sudo pip3 install RPi.GPIO
sudo pip3 install spidev
```   
Clone this repository
```bash
cd ~
git clone https://github.com/mikrokontrolerpl/trelloToDoList
``` 
## Environment Variables

To run this project, you will need to add the following environment variables to your keys.dat file

`Trello API key`

`Trello Token`

`Trello Board ID`

`Trello List name`

## cron
To run the script periodically, add to the crontab following line:

`*/5 * * * * bash ~/trelloToDoList/code/update.sh`
## License

[MIT](https://choosealicense.com/licenses/mit/)


## Related

Here are some related projects

[Trello Parsers API](https://github.com/abhinuvpitale/Trello-Raspberry-Pi-Zero-API)

[e-Paper display library](https://github.com/waveshare/e-Paper)

[The project idea](https://www.raspberrypi.com/news/build-an-e-paper-to-do-list-with-raspberry-pi/)
