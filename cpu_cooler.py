import hid
from threading import Event, Thread
import psutil

def get_cpu_temp():
    temp = psutil.sensors_temperatures()['k10temp'][0].current
    return temp

VENDOR_ID = 0xaa88
PRODUCT_ID = 0x8666

device = hid.Device(VENDOR_ID, PRODUCT_ID)

def write_to_cpu_fan_display(dev):
    fCpuTemp = get_cpu_temp()

    byte_comands = bytes([0, int(fCpuTemp)])

    try:
        num_bytes_written = dev.write(byte_comands)
    except IOError as e:
        print ('Error writing command: {}'.format(e))
        return None 

    return num_bytes_written

def call_repeatedly(interval, func, *args):
    stopped = Event()
    def loop():
        while not stopped.wait(interval):
            func(*args)
    Thread(target=loop).start()    
    return stopped.set

print('Connected to {}\n'.format(PRODUCT_ID))

seconds = 1
cancel_future_calls = call_repeatedly(seconds, write_to_cpu_fan_display, device)
