# TradeShowButtons
Proof of Concept for HIMMS

This proof of concept was for an idea we had for a trade show. Our representives would pass out M&Ms of the company's colors, green purple and blue. Then,
a physical button of the corresponding color would be pressing, updating a live analyics dashboard in our booth. 

This code is in Circut Python, a derivative of MicroPython and Pythong, designed to run on microcontrollers. 

This code ran on an Adafruit Metro M4.

On boot, a WiFi connection is estabilished, and then every time a button is pressed, a POST API call is made to server, sending the color M&M choosen 
by the attendee of the conference. 
