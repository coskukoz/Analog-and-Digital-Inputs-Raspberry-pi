import spidev
import time
import os
import urllib
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)


spi = spidev.SpiDev()
spi.open(0,0)


def ReadChannel(channel):
  adc = spi.xfer2([1,(8+channel)<<4,0])
  data = ((adc[1]&3) << 8) + adc[2]
  return data



def ConvertVolts(data,places):
  volts = (data * 10) / float(1023)
  volts = round(volts,places)  
  return volts


  

  
sensor1_channel = 0
sensor2_channel = 1
sensor3_channel = 2
sensor4_channel = 3
sensor5_channel = 4
sensor6_channel = 5
sensor7_channel = 6
sensor8_channel = 7
delay = 5


GPIO.setwarnings(False)
GPIO.setup(5, GPIO.IN)
GPIO.setup(6, GPIO.IN)
GPIO.setup(13, GPIO.IN)
GPIO.setup(19, GPIO.IN)
GPIO.setup(26, GPIO.IN)
GPIO.setup(16, GPIO.IN)
GPIO.setup(20, GPIO.IN)
GPIO.setup(21, GPIO.IN)
    
  

while True:


        
  foldtime = time.time()
  fnewtime = time.time()
  fstore = 900.0                                 # second

  while True:  
    fnewtime = time.time()
    fdtime = fnewtime-foldtime


  
    digital1 = GPIO.input(5)
    digital2 = GPIO.input(6)
    digital3 = GPIO.input(13)
    digital4 = GPIO.input(19)
    digital5 = GPIO.input(26)
    digital6 = GPIO.input(21)
    digital7 = GPIO.input(20)
    digital8 = GPIO.input(16)

    if digital1 == 1:
     digital1 = 'ON'
    else:
      digital1 = 'OFF'

    if digital2 == 1:
     digital2 = 'ON'
    else:
      digital2 = 'OFF'

    if digital3 == 1:
     digital3 = 'ON'
    else:
      digital3 = 'OFF'

    if digital4 == 1:
     digital4 = 'ON'
    else:
      digital4 = 'OFF'

    if digital5 == 1:
     digital5 = 'ON'
    else:
      digital5 = 'OFF'

    if digital6 == 1:
     digital6 = 'ON'
    else:
      digital6 = 'OFF'

    if digital7 == 1:
     digital7 = 'ON'
    else:
      digital7 = 'OFF'

    if digital8 == 1:
     digital8 = 'ON'
    else:
      digital8 = 'OFF'


    sensor1_level = ReadChannel(sensor1_channel)
    sensor1_volts = ConvertVolts(sensor1_level,2)
  
    sensor2_level = ReadChannel(sensor2_channel)
    sensor2_volts = ConvertVolts(sensor2_level,2)
  
    sensor3_level = ReadChannel(sensor3_channel)
    sensor3_volts = ConvertVolts(sensor3_level,2)

    sensor4_level = ReadChannel(sensor4_channel)
    sensor4_volts = ConvertVolts(sensor4_level,2)

    sensor5_level = ReadChannel(sensor5_channel)
    sensor5_volts = ConvertVolts(sensor5_level,2)

    sensor6_level = ReadChannel(sensor6_channel)
    sensor6_volts = ConvertVolts(sensor6_level,2)

    sensor7_level = ReadChannel(sensor7_channel)
    sensor7_volts = ConvertVolts(sensor7_level,2)

    sensor8_level = ReadChannel(sensor8_channel)
    sensor8_volts = ConvertVolts(sensor8_level,2)


    if fdtime >= fstore:
      foldtime = fnewtime
      googlepage = "https://script.google.com/macros/s/"
      mygooglekey = "AKfycbysdfsdfsdfsdfskqtjr_0wSgFJKfqR6s21QtLeO9oJMhUqzFBs" // 
      wtime = time.strftime("%d/%m/%Y %H:%M:%S")
      content = urllib.urlopen("%s%s/exec?DATE=%s&Sensor1=%s&Sensor2=%s&Sensor3=%s&Sensor4=%s&Sensor5=%s&Sensor6=%s&Sensor7=%s&Sensor8=%s&Digital1=%s&Digital2=%s&Digital3=%s&Digital4=%s&Digital5=%s&Digital6=%s&Digital7=%s&Digital8=%s" %(googlepage, mygooglekey, wtime, sensor1_volts, sensor2_volts, sensor3_volts, sensor4_volts, sensor5_volts, sensor6_volts, sensor7_volts, sensor8_volts, digital1, digital2, digital3, digital4, digital5, digital6, digital7, digital8)).read()
      print "-----------------------------------------------------------------------------"  
      print(" Sensor-1            Sensor-2         Sensor-3          Sensor-4         Sensor-5            Sensor-6         Sensor-7          Sensor-8")
      print(" {} - ({}V)        {} - ({}V)      {} - ({}V)      {} - ({}V)          {} - ({}V)          {} - ({}V)     {} - ({}V)        {} - ({}V)".format(sensor1_level,sensor1_volts,sensor2_level,sensor2_volts,sensor3_level,sensor3_volts,sensor4_level,sensor4_volts,sensor5_level,sensor5_volts,sensor6_level,sensor6_volts,sensor7_level,sensor7_volts,sensor8_level,sensor8_volts))    
      print(" Digital-1            Digital-2         Digital-3          Digital-4         Digital-5            Digital-6         Digital-7          Digital-8")
      print(" {}                  {}                  {}                 {}                    {}                    {}                {}                 {} ".format(digital1,digital2,digital3,digital4,digital5,digital6,digital7,digital8))    


time.sleep(delay)











