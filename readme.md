# BabyMon
**BabyMon** is a motion-sensing (coming-soon), temperature-detecting (coming-soon), night-vision-capable video surveillance baby monitor.

## Hardware Requirements
In order for this project to run properly, you must have the following hardware:
1. Raspberry Pi (I'm using [model 3B](https://www.adafruit.com/product/3775))
2. One of the following:
- [Raspberry Pi Nightvision Camera](https://www.amazon.com/gp/product/B0759GYR51/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1) - Works well in low-light. Includes infrared emitter & sensors.
- [Raspberry Pi Noir Camera](https://www.amazon.com/Raspberry-Pi-Camera-Module-1080P30/dp/B071WP53K7/ref=sr_1_2_sspa?crid=24AXW3MYYS8ZQ&keywords=raspberry+pi+noir+camera&qid=1562121436&s=electronics&sprefix=raspberry+pi+Noir+Cam%2Cmobile%2C135&sr=1-2-spons&psc=1) - works well if you have a separate infrared light emitter
- [Raspberry Pi Camera Module](https://www.amazon.com/Raspberry-Pi-Camera-Module-Megapixel/dp/B01ER2SKFS) - only works well during the day
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
