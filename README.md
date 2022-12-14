# TradeShowButtons
## Proof of Concept for HIMMS 2022


This proof of concept was for an idea we had for a trade show. Our representives would pass out M&Ms of the company's colors: green, purple and blue. Then,
a physical button of the corresponding color would be pressed, updating a live analyics dashboad, shown on a monitor in our booth. 

This code is in Circut Python, a derivative of MicroPython and Python, which is a language for low entry microcontroller programming. 

This code ran on an Adafruit Metro M4 Express AirLift, a ATSAMD51 development board which also has a ESP32 co-processor for WiFi & bluetooth communications. 
Product page for this development board: <https://www.adafruit.com/product/4000>

On boot, a WiFi connection is estabilished, and then every time a button is pressed, a POST API call is made to server, sending the color of M&M choosen 
by the attendee of the conference. 

As a proof of concept this code was written in an hour or two, and could admittedly, use a cleanup. 
