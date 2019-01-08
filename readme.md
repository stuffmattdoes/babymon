# BabyMon
**BabyMon** is a motion-sensing, temperature-detecting, night-vision-capable video surveillance baby monitor.

## Hardware Requirements
In order for this project to run properly, you must have the following hardware:
1. Raspberry Pi (I'm using [model 3B](https://www.adafruit.com/product/3775))
2. [Raspberry Pi Camera Module](https://www.amazon.com/Raspberry-Pi-Camera-Module-Megapixel/dp/B01ER2SKFS)
3. (Optional) [Motion sensor](https://www.gearbest.com/development-boards/pp_70386.html)
4. (Optional) Microphone (can be [USB](https://www.adafruit.com/product/3367) or [GPIO](https://www.amazon.com/Adafruit-Electret-Microphone-Amplifier-MAX9814/dp/B00SLYAI9K))
5. (Optional) [Temperature sensor](https://www.amazon.com/Gowoops-Temperature-Humidity-Measurement-Raspberry/dp/B073F472JL)
6. A reall neat [RPi & camera case!](https://smarticase.com/collections/all/products/smartipi-kit-3?variant=4366898177)

## Setup
1. Make sure your client computer and raspberry pi are on the same network.
2. In command line, run `python3 server.py` and visit `<RaspberryPiIP>:8000` in your browser!
* Note - `<RaspberryPiIP>` should be your raspberry pi's IP address - such as `192.168.1.24`

## Resources
[PiCamera Web Streaming](https://picamera.readthedocs.io/en/release-1.13/recipes2.html#web-streaming)
