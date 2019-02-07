import time
import serial

file=open("arduino.dat","a")
file.write("\n")

s=serial.Serial('/dev/ttyUSB0',9600)


while True:
 t=time.localtime(time.time())
 #time.struct_time(tm_year=2010, tm_mon=2, tm_mday=7, tm_hour=14, tm_min=46, tm_sec=58, tm_wday=6, tm_yday=38, tm_isdst=0)
 year=t.tm_year
 mon=t.tm_mon
 mday=t.tm_mday
 hour=t.tm_hour
 min=t.tm_min
 min0=""
 n1=0
 sec=t.tm_sec

 data =""
 try:
  data = s.readline()
 except SerialException:
  print "Error reading serial port"
# print data
 print year,mon,mday,hour,min,sec,data
 file.write("%s %s %s %s %s %s %s" % (year,mon,mday,hour,min,sec,data))
 file.flush()
 
 
