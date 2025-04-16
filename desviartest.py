from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait, StopWatch
from enviar import main_to_sec
hub = PrimeHub(observe_channels=[125])


sensor_esquerdo = ColorSensor(Port.C)
sensor_direito = ColorSensor(Port.A)
senaoraux = ColorSensor(Port.E)
mt = Motor(Port.F)
me = Motor(Port.D)
md = Motor(Port.B)

def mover():
    md.run_time(100, 1000)
    me.run_time(-100, 1000)
    mt.run_time(100, 500)

mover()