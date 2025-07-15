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


LIMIAR_PRETO = 40
PPP = 35
PP = 50
VELOCIDADE_BASE = 160

# ROBÔ ANDAR PARA FRENTE
def mover_para_frente():
    velocidade = 400  # Velocidade dos motores
    tempo = 3000  # Tempo de movimento em milissegundos (simulando millis())

    # Iniciando o cronômetro
    stopwatch = StopWatch()
    
    # Inicia os motores ao mesmo tempo
    md.run(velocidade)  # Motor Direito
    me.run(-velocidade)  # Motor Esquerdo
   
    
    # Aguarda até que o tempo especificado tenha passado
    while stopwatch.time() < tempo:
        pass  # Aguarda até o tempo passar (sem bloquear outras execuções)

    # Após o tempo, para o movimento
    md.stop()
    me.stop()


# 90º ESQUERDA
def nove(): 
    me.run(200)
    md.run(200)
    mt.run(200)
    wait(3000)


# 90º DIERITA
def novd(): 
    me.run(-200)
    md.run(-200)
    mt.run(-200)
    wait(3000)