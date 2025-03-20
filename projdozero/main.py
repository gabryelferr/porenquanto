from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase

#SENSORES E MOTORES
sensor_esquerdo = ColorSensor(Port.C)
sensor_direito = ColorSensor(Port.A) 

me = Motor(Port.D) 
mt = Motor(Port.F) 
md = Motor(Port.B)


        
# Função para seguir linha
def seguir_linha():
    while True:

        print(sensor_esquerdo.reflection())

        # Obter leituras dos sensores de cor (0 a 100 de intensidade de luz refletida)
        se = sensor_esquerdo.reflection()
        sd = sensor_direito.reflection()

        # Definir linha para distinguir entre preto e branco
        linha = 50  # Ajuste esse valor conforme necessário

        if se > linha and sd > linha:
            # Ambos os sensores no preto -> Seguir reto
            md.run(160)
            me.run(-160)
            mt.run(0)  # Manter reta

        elif se > linha and sd <= linha:
            # Sensor direito saiu da linha -> Ajustar para direita
            md.run(-160)
            me.run(-280)
            mt.run(-280)  # Girar para direita

        elif se <= linha and sd > linha:
            # Sensor esquerdo saiu da linha -> Ajustar para esquerda
            md.run(160)
            me.run(280)
            mt.run(280)  # Girar para esquerda
        
        else:
            # Ambos fora da linha -> Parar
            md.stop()
            me.stop()
            mt.stop()

        wait(50)  # Pequeno atraso para estabilidade

# Chamando a função principal
seguir_linha()

