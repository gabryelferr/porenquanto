from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait, StopWatch
from pybricks.parameters import Axis
hub = PrimeHub(observe_channels=[125])

def detectar_preto(sensor):
    h, s, v = sensor.hsv()
    print(f"[PRETO] HSV: h={h}, s={s}, v={v}")
    return (170 <= h <= 220) and (20 > s) and (38 > v > 5)


def detectar_verde(sensor):
    h, s, v = sensor.hsv()
    print(f"[VERDE]  HSV detectado: h={h}, s={s}, v={v}")
    return (148 <= h <= 158) and (85 > s > 60) and (50 > v > 28)


def detectar_vermelho(sensor):
    h, s, v = sensor.hsv()
    print(f"HSV detectado: h={h}, s={s}, v={v}")
    return (h >= 340) and (85 > s > 75) and (60 > v > 45)