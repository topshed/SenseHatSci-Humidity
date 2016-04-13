import logging
from twoDigit.twoDigit import numToMatrix
from sense_hat import SenseHat
from datetime import datetime
from time import sleep

# Set up the logfile name based on date/time
logfile = "humidity-"+str(datetime.now().strftime("%Y%m%d-%H%M"))+".csv"
# Logging settings and format for csv
logging.basicConfig(filename=logfile, level=logging.DEBUG,
    format='%(asctime)s %(message)s',
    datefmt='%Y-%m-%d, %H:%M:%S,')

sh = SenseHat() # Connect to SenseHAT
h_old = 0
col = [0,0,255]

while True: # main loop

   h = sh.get_humidity() # Take humidity reading
   logging.info(str(h)) # Log value to file
   if h > h_old: # If humdiity has increased...
       col = [255,0,0] # Set to Red
   else: # If humidity has decreased...
       col = [0,255,0] # set to green

   h = int(round(h,0)) # round to a whole precent
   i = numToMatrix(h,col) #create 2 digit image for matrix
   sh.set_pixels(i) # display reading
   sleep(0.5)
   h_old = h # Set previous value
