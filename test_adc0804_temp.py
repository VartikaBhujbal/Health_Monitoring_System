import RPi.GPIO as IO                   # calling for header file which helps us use GPIO’s of PI
import time                             # calling for time to provide delays in program

IO.setwarnings(False)                   # do not show any warnings
IO.setmode (IO.BCM)                     # programming the GPIO by BCM pin numbers. (like PIN29 as‘GPIO5’)

digital_value=1
decimal_places = 1
delay1 = 0.001                          # 1ms
delay2 = 0.01                           # 10ms
delay3 = 1                              # 1s

IO.setup(4,IO.IN)                       # initialize GPIO Pins as input
IO.setup(17,IO.IN)
IO.setup(27,IO.IN)
IO.setup(22,IO.IN)
IO.setup(5,IO.IN)
IO.setup(6,IO.IN)
IO.setup(13,IO.IN)
IO.setup(19,IO.IN)

def Read_ADC():
    b0=b1=b2=b3=b4=b5=b6=b7=0           # reset values
    
    if (IO.input(19) == True):
        time.sleep(delay1)
        if (IO.input(19) == True):
            b7=1                        # if pin19 is high bit7 is true

    if (IO.input(13) == True):
        time.sleep(delay1)
        if (IO.input(13) == True):
            b6=1                        # if pin13 is high bit6 is true

    if (IO.input(6) == True):
        time.sleep(delay1)
        if (IO.input(6) == True):
            b5=1                        # if pin6 is high bit5 is true

    if (IO.input(5) == True):
        time.sleep(delay1)
        if (IO.input(5) == True):
            b4=1                        # if pin5 is high bit4 is true

    if (IO.input(22) == True):
        time.sleep(delay1)
        if (IO.input(22) == True):
            b3=1                        # if pin22 is high bit3 is true

    if (IO.input(27) == True):
        time.sleep(delay1)
        if (IO.input(27) == True):
            b2=1                        # if pin27 is high bit2 is true
 
    if (IO.input(17) == True):
        time.sleep(delay1)
        if (IO.input(17) == True):
            b1=1                        # if pin17 is high bit1 is true

    if (IO.input(4) == True):
        time.sleep(delay1)
        if (IO.input(4) == True):
            b0=1                        # if pin4 is high bit0 is true

    # representing the bit values from LSB to MSB
    digital_value = (1*b0)+(2*b1)+(4*b2)+(8*b3)+(16*b4)+(32*b5)+(64*b6)+(128*b7)   
    time.sleep(delay2)                    # wait for 10ms 
    return digital_value

def ConvertTemp(data, places):
    temp = ((data * 500)/float(256))
    temp = round(temp, places)
    return temp

while True:
    temp_level = Read_ADC()
    temp = ConvertTemp(temp_level, decimal_places)

    print("Temperature : {} ({} C)".format(temp_level, temp))
    time.sleep(delay3)



                                     
