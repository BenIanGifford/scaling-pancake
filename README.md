# scaling-pancake
Vending machine code for the onion omega

# GPIO setup

The light gate is set using a ground pin, 3.3V pin, and pin 2 as sig

The "motor" is currently only wired as an LED off of a ground pin, and pin 1

# Installation 

Use the v0.1.0-alpha release

`wget https://github.com/BenIanGifford/scaling-pancake/archive/refs/tags/alpha.zip`

`unzip ./alpha.zip`

# Library setup

This requires the onion-gpio-sysfs library put together by Deric-W and the paho-mqtt library from eclipse

## GPIO library

Installation is as follows:

`wget -O oniongpio.zip https://github.com/Deric-W/onion-gpio-sysfs/archive/refs/tags/0.3.zip`

Downloads the zip file from github and saves it as oniongpio.zip

`unzip ./oniongpio.zip`

Unzips it to ./onion-gpio-sysfs-0.3

`cp ./onion-gpio-sysfs-0.3/onionGpio.py /usr/lib/python3.6/onionGpio.py`

Moves the library file to /usr/lib so it can be imported from anywhere

Then if space is an issue everything else can be removed with
`rm -rv ./onion-gpio-sysfs-0.3 oniongpio.zip`

## MQTT library

`pip install paho-mqtt`
