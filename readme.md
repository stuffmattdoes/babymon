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
2. In command line, run `python3 server.py` and visit `<RaspberryPiIP>` in your browser!
* Note - `<RaspberryPiIP>` should be your raspberry pi's IP address - such as `192.168.1.24`. ALternatively, you can access your Raspberry Pi at `<hostname>.local`, where `hostname` is whatever you've configured on your Raspberry Pi (`raspberrypi` by default). More on that [here](https://thepihut.com/blogs/raspberry-pi-tutorials/1966 8676-renaming-your-raspberry-pi-the-hostname).

### Run BabyMon on Pi startup
I want my baby monitor to run automatically each time I plug in the Raspberry Pi, that way I don't have to manually VNC in and run the script. There are a few ways to automatically run scripts on boot:
- Adding a line in `rc.local`
- Adding a line in `.bashrc`
- Creating a new `init.d` tab
- systemd
- crontab

I've opted for the `rc.local` method. You can read more on accomplishing the other methods [here](https://www.dexterindustries.com/howto/run-a-program-on-your-raspberry-pi-at-startup/)

While logged into your Pi in terminal, edit `/etc/rc.local` with the following line:
`cd /home/pi/path/to/babymon && python3 server.py &`
Since the contents of `rc.local` are executed on system boot, our baby monitor script will run! Note the `&` at the end of the command. This allows us to fork our baby monitor process since it runs an infinite loop, which would prevent the `rc.local` script from proceeding its execution.

## Resources
[PiCamera Web Streaming](https://picamera.readthedocs.io/en/release-1.13/recipes2.html#web-streaming)

## Todo
1. ~~Stream video from Pi to network upon client request~~
2. 

2. Separate camera code from network server code
+ Have Pi cameras feed video to central Pi server
+ Central Pi server streams to client upon request
3. Sound
4. Temperature
5. Motion capture
+ If motion is detected, capture video feed on server (store for...1 week?)
+ If connected to a client, video is streamed regardless of motion