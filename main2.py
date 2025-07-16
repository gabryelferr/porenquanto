from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait, StopWatch
hub = PrimeHub(observe_channels=[125])


sensor_esquerdo = ColorSensor(Port.C)
sensor_direito = ColorSensor(Port.A)
senaoraux = ColorSensor(Port.E)
mt = Motor(Port.F)
me = Motor(Port.D)
md = Motor(Port.B)

se = sensor_esquerdo.reflection()
sd = sensor_direito.reflection()

LIMIAR_PRETO = 17
VELOCIDADE_BASE = 200



def definir_velocidade(motor, velocidade):
    motor.run(velocidade)

def detectar_preto(sensor):
    h, s, v = sensor.hsv()
    print(f"[PRETO] HSV: h={h}, s={s}, v={v}")
    return (170 <= h <= 220) and (20 > s) and (38 > v > 5)


def seguir_linha():
    while True:
        se = sensor_esquerdo.reflection()
        sd = sensor_direito.reflection()
        print(f"se: {se}, sd: {sd}")

        # Seguir em linha reta
        if se > LIMIAR_PRETO and sd > LIMIAR_PRETO:
             definir_velocidade(md, VELOCIDADE_BASE)
             definir_velocidade(me, -VELOCIDADE_BASE)
             mt.run(0)  # Manter reta

        #  Curva para direita
        elif se > LIMIAR_PRETO and sd <= LIMIAR_PRETO:
             definir_velocidade(md, -200)
             definir_velocidade(me, -290)
             mt.run(-500)

         # Curva para esquerda
        elif se <= LIMIAR_PRETO and sd > LIMIAR_PRETO:
             definir_velocidade(me, 200)
             definir_velocidade(md, 290)
             mt.run(500)


        wait(50)  # Pequeno atraso para estabilidade


def rodarcodigo():
    seguir_linha()


rodarcodigo()