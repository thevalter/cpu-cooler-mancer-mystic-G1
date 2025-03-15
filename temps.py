import hid
from threading import Event, Thread
import psutil

print(psutil.sensors_temperatures());

def get_cpu_temp():
    temp = psutil.sensors_temperatures()['k10temp'][0].current
    return temp

fCpuTemp = get_cpu_temp()


