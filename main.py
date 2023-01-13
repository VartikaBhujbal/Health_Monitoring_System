'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
Project Name    :   Raspberry Pi Based heartrate pulse oxymetry and temperature
                    measurement with GSM & Thinkspeak cloud interfacing
                    [or]
                    Smart Patient Monitoring System [SPM System]
Main Hardware   :   Raspberry Pi 3 model B+
Processor       :   ARMv8-A (Quad 32/64 bit)
SoC IC          :   BCM2837B0
OS Requirement  :   Debian Raspbian
Linux Version   :   Linux 4.19.0      
Other Hardwares :   ADC 0804, LM35, max30100
Session Year    :   Mar-Apr 2021
Developed By    :   Kashish, Kanchan, Khyati, Nancy, Ojaswini
Developed for   :   Oriental Institute of Science & Technology, Bhopal
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
=================================== Start of Program ==================================
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
importing header files 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
import time
import urllib3                                          # for thingspeak
import max30100                                         # for max30100 sensor
import RPi.GPIO as IO                                   # for GPIO's of Pi
from twilio.rest import Client                          # for sms gateway

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
variables & function for sms gateway 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'''
#Ojaswini Panse
account_sid="AC08ee9e38773ddcc965db378a71dc6967"	# Account Serial ID
auth_token="855484507717aafe568ec3c8c3223496"		# Authentication token
sender_no="+18157707381"				# Number provided by twilio
receiver_no="+918770764317"				# Number verified by twilio

# Nancy Bansal
account_sid="ACb7b83be58baf782ffccd764485c7f567"	# Account Serial ID
auth_token="5cf7dee18ea922695e30ee53da772cac"		# Authentication token
sender_no="+13342268236"				# Number provided by twilio
receiver_no="+919893875625"				# Number verified by twilio

#Kashish agarwal
account_sid="AC9d1f744032a24fab127aa1d7db96631f"	# Account Serial ID
auth_token="f7e89bcf4e08b41ecf5fd1cb41055de3"		# Authentication token
sender_no="+18312988290"				# Number provided by twilio
receiver_no="+919926464640"				# Number verified by twilio

#Kanchan Bhujbal
account_sid="AC9e29f71ab329df9d836544a4947df17d"	# Account Serial ID
auth_token="1b704161ccb41ce32c52fd47493fb1e2"		# Authentication token
sender_no="+14156399902"				# Number provided by twilio
receiver_no="+917869836993"				# Number verified by twilio
'''
#Khyati Sengar
account_sid="AC4a6d0e604ef0743f8c366345f6d1e466"	# Account Serial ID
auth_token="288c61322b82c94a3d26bf67d9ff156e"		# Authentication token
sender_no="+19293252911"				# Number provided by twilio
receiver_no="+917400752978"				# Number verified by twilio

msg="Welcome to the SPM System ... [get PData in 1min]" # Default message
                                                        
def Send_SMS():    
    client=Client(account_sid, auth_token)
    client.messages.create(from_=sender_no, body=msg, to=receiver_no)                           

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
function for thingspeak
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def Cloud_Upload():
    req = urllib3.PoolManager()                         # Request
    res = req.request('Post',url)                       # Responce

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
creating object for max30100 sensor
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
mx30 = max30100.MAX30100()
mx30.enable_spo2() 

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
functions for ADC
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
IO.setwarnings(False)                                   # setting for no warnings
IO.setmode (IO.BCM)                                     # BCM Mode

IO.setup(4,IO.IN)                                       # RPi GPIO-pin setting                   
IO.setup(17,IO.IN)
IO.setup(27,IO.IN)
IO.setup(22,IO.IN)
IO.setup(5,IO.IN)
IO.setup(6,IO.IN)
IO.setup(13,IO.IN)
IO.setup(19,IO.IN)

def Read_ADC():                                         # function to get decimal value
    b0=b1=b2=b3=b4=b5=b6=b7=0        
    if (IO.input(19) == True):
        time.sleep(0.001)
        if (IO.input(19) == True):
            b7=1                        
    if (IO.input(13) == True):
        time.sleep(0.001)
        if (IO.input(13) == True):
            b6=1                        
    if (IO.input(6) == True):
        time.sleep(0.001)
        if (IO.input(6) == True):
            b5=1                        
    if (IO.input(5) == True):
        time.sleep(0.001)
        if (IO.input(5) == True):
            b4=1                        
    if (IO.input(22) == True):
        time.sleep(0.001)
        if (IO.input(22) == True):
            b3=1                        
    if (IO.input(27) == True):
        time.sleep(0.001)
        if (IO.input(27) == True):
            b2=1                         
    if (IO.input(17) == True):
        time.sleep(0.001)
        if (IO.input(17) == True):
            b1=1                        
    if (IO.input(4) == True):
        time.sleep(0.001)
        if (IO.input(4) == True):
            b0=1                        
    analog_value = (1*b0)+(2*b1)+(4*b2)+(8*b3)+(16*b4)+(32*b5)+(64*b6)+(128*b7)   
    time.sleep(0.01)                    
    return analog_value

def ConvertTemp(data, places):                          # function to get temperature
    temp_in_C = ((data * 500)/float(256))               # in Celsius
    temp_in_F = ((temp_in_C * 9)/float(5)) + 32         # in Fahrenheit
    temperature = round(temp_in_F, places)
    return temperature

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
main program
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while True:
    Send_SMS()                                         # sending message in every min
    for x in range (0,7):                               # loop for one min

        for i in range(0,100):                          # max30100 working
            mx30.read_sensor()
        mx30.ir, mx30.red
        hb = int(mx30.ir / 100)
        spo2 = int(mx30.red / 100)
        if mx30.ir != mx30.buffer_ir :
            print("Pulse : {} BPM,".format(hb))
        if mx30.red != mx30.buffer_red:
            print("SPO2 : {} %".format(spo2))
        
        temp_level = Read_ADC()                         # ADC0804 & LM35 working
        temp = ConvertTemp(temp_level, 1)
        print("Temperature : {} deg F.".format(temp))  

        t=str(temp)                                     # convertion of data into string
        h=str(hb)
        o=str(spo2)

                                                        # data uploading
        url = "https://api.thingspeak.com/update?api_key=YPIH5SAYWH4I9ALT&field1=%s&field2=%s&field3=%s" %(t,h,o)
        Cloud_Upload()
        
                                                        # update message for sms
        msg = "City Hospital, Bhopal, PID#xxx, Temp:{} dF, HR:{} BPM, SPO2:{} %".format(t,h,o)
        time.sleep(10)     

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
==================================== End of Program =================================== 
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
