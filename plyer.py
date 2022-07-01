from kivy.utils import platform
from plyer.facades.accelerometer import Accelerometer
from plyer.facades.gyroscope import Gyroscope
from plyer.facades.bluetooth import Bluetooth
from plyer import gps 
from android.permission import request_permissions, Permission
#https://www.youtube.com/watch?v=A9Rahw6c3eY


def accAccelerometer():
    Accelerometer.enable()
def denyAccelerometer():
    Accelerometer.disable()
def accGyro():
    Gyroscope.enable()
def denyGyro():
    Gyroscope.disable()
def accBluetooth():
    Bluetooth.enable()
def denyGyro():
    Bluetooth.disable()

def accMemory():
    if platform=="android":
        request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])

