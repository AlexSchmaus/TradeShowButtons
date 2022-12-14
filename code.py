# Metro M4 AirLift IO demo
# Welcome to CircuitPython 4 :)

import time
import board
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn
import neopixel
import busio
import audioio
import pulseio
import simpleio


import adafruit_esp32spi.adafruit_esp32spi_socket as socket
from adafruit_esp32spi import adafruit_esp32spi
import adafruit_requests as requests


try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

# If you are using a board with pre-defined ESP32 Pins:
esp32_cs = DigitalInOut(board.ESP_CS)
esp32_ready = DigitalInOut(board.ESP_BUSY)
esp32_reset = DigitalInOut(board.ESP_RESET)

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset)

print("Connecting to AP...")
while not esp.is_connected:
    try:
        esp.connect_AP(secrets["ssid"], secrets["password"])
    except RuntimeError as e:
        print("could not connect to AP, retrying: ", e)
        continue
print("Connected to", str(esp.ssid, "utf-8"), "\tRSSI:", esp.rssi)

# Initialize a requests object with a socket and esp32spi interface
socket.set_interface(esp)
requests.set_socket(socket, esp)

DEMO_URL = "http://192.168.20.128:3000"


# One pixel connected internally!
dot = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.2)

# Built in red LED
led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

# Initialize WiFi Module
if esp.status == adafruit_esp32spi.WL_IDLE_STATUS:
    print("ESP32 found and in idle mode")
print("Firmware vers.", esp.firmware_version)
print("MAC addr:", [hex(i) for i in esp.MAC_address])

# Digital input with pullup on D2, D3, and D4
buttons = []
for p in [board.D0, board.D1, board.D2]:
    button = DigitalInOut(p)
    button.direction = Direction.INPUT
    button.pull = Pull.DOWN
    buttons.append(button)


######################### HELPERS ##############################

# Helper to give us a nice color swirl
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if (pos < 0):
        return [0, 0, 0]
    if (pos > 255):
        return [0, 0, 0]
    if (pos < 85):
        return [int(pos * 3), int(255 - (pos*3)), 0]
    elif (pos < 170):
        pos -= 85
        return [int(255 - pos*3), 0, int(pos*3)]
    else:
        pos -= 170
        return [0, int(pos*3), int(255 - pos*3)]


######################### MAIN LOOP ##############################

i = 0
while True:

  # spin internal LED around! autoshow is on
  dot[0] = wheel(i & 255)

  if buttons[0].value:
      data = {"color":"GREEN", "count":1}
      res2 = requests.post(DEMO_URL + "/submitMM", json=data)
      print(res2.text)
      res2.close()
      print("Button D2 pressed!", end ="\t")

  if buttons[1].value:
      data = {"color":"BLUE", "count":1}
      res2 = requests.post(DEMO_URL + "/submitMM", json=data)
      print(res2.text)
      res2.close()
      print("Button D3 pressed!", end ="\t")

  if buttons[2].value:
      data = {"color":"PURPLE", "count":1}
      res2 = requests.post(DEMO_URL + "/submitMM", json=data)
      print(res2.text)
      res2.close()
      print("Button D4 pressed!", end ="\t")




  i = (i+1) % 256  # run from 0 to 255
  time.sleep(0.1) # make bigger to slow down

  print(i)