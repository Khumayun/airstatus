# airstatus

This is a Django Rest API project for collecting data from several sensors:
  1. Plantower 5003 - for counting the quantity of dust in the space with diameters in the following ranges: 0.3 - 1.0 | 1.0 - 2.5 | 2.5 - 10 micrometers.
    for more about sensor - http://www.plantower.com/en/content/?108.html
  2. DHT11 - for measuring the humidity and temperature.
  3. MHZ-19B - for measuring CO2 concentration in the space. units - PPM

Please visit http://104.248.198.113/ to see demo.
Front-end for this project is made on React.js framework and Chartjs v2 library. source code - https://gitlab.com/Abbos1994/react-weather
C code is available here - https://github.com/Khumayun/airstatus_arduino/

Project overview:

NodeMCU v3 connected to 3 sensor using different protocols.
Every time perion (30 min) creates a POST request to DRF, then it saves data to Postgresql.
And finally you can see the data on the web-site using date filter.
Chartjs is awesome visualisation for this type of data.


MIT Licence №HF934H9HGOIH34G.

just kidding :)
