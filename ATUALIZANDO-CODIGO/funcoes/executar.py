from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait, StopWatch
from pybricks.parameters import Axis
hub = PrimeHub(observe_channels=[125])



sensor_esquerdo = ColorSensor(Port.C)
sensor_direito = ColorSensor(Port.A)
sensoraux = ColorSensor(Port.E)
mt = Motor(Port.F)
me = Motor(Port.D)
md = Motor(Port.B)


# CALIBRAÇÃO DE SENSORES
LIMIAR_PRETO = 40
# PPP = 35
PP = 50
VELOCIDADE_BASE = 160


# Gira 90º esquerda
def nove(): 
    me.run(200)
    md.run(200)
    mt.run(200)
    wait(1600)


# Gira 90º direita
def novd(): 
    me.run(-200)
    md.run(-200)
    mt.run(-200)
    wait(1600)


# Quando o robô ver verde, ele irá executar alguma das ações abaixo
def executar_verde():
    parar_motor()  # Para os motores antes de executar a lógica
    hub.speaker.beep(1000, 700)  # Emite um som para indicar que viu verde
    print("É VERDE — Executando lógica especial")

    # Move os motores da direita e esquerda em direções opostas e depois para eles
    me.run(-100)
    md.run(100)
    mt.run(0)
    wait(50)
    parar_motor()
    wait(100)

    # Executa a lógica de detecção de verde
    esq_verde = detectar_verde(sensor_esquerdo)
    dir_verde = detectar_verde(sensor_direito)

    # AMBOS os sensores veem verde -> dar meia volta
    if esq_verde and dir_verde:
        hub.speaker.beep(800, 700)  # Emite um som para indicar que ambos os sensores viram verde
        # variavel_verde = 3  # Atualiza a variável para indicar que os sensores estão vendo verde
        print("VERDE NOS DOIS SENSORES")

        # Realiza o movimento de rotação de 360 graus
        me.run(100)  # Motor esquerdo gira para frente
        md.run(-100)  # Motor direito gira para trás
        wait(2000)  # Tempo para completar o giro de 360 graus
        
        # Para a rotação e ajusta o robô para seguir no sentido contrário
        me.run(-100)  # Motor esquerdo agora vai para trás
        md.run(100)  # Motor direito agora vai para frente

        wait(1000)  # Aguarda um tempo para garantir que o robô está seguindo a linha no sentido oposto

        # Parando os motores após o movimento
        parar_motor()  
        novd()  #Gira 90 graus para a direita
        parar_motor()  # Garante que todos os motores parem
        wait(100)  # Pausa adicional
        novd()  
        parar_motor()  # Garante a parada final dos motores

    # Sensor ESQUERDO vê verde -> girar para a esquerda
    elif esq_verde: 
        print("VERDE NO SENSOR ESQUERDO")
        me.run(-100)
        md.run(100)
        mt.run(0)
        wait(1200)

        relogio = StopWatch()
        relogio.reset()

        me.run(150)
        md.run(150)
        mt.run(150)

        while relogio.time() < 5000:
            if sensor_esquerdo.reflection() < LIMIAR_PRETO:
                print("SENSOR VIU PRETO")
                me.stop()
                md.stop()
                mt.stop()
                break
        wait(10)
        parar_motor()
        wait(100)

    # Sensor DIREITO vê verde -> girar para a direita'
    elif dir_verde:
        variavel_verde = 1
        print("VERDE NO SENSOR DIRETO")
        me.run(-100)
        md.run(100)
        mt.run(0)
        wait(1200)

        relogio = StopWatch()
        relogio.reset()

        me.run(-150)
        md.run(-150)
        mt.run(-150)

        while relogio.time() < 5000:
            if sensor_direito.reflection() < LIMIAR_PRETO:
                print("SENSOR VIU PRETO")
                me.stop()
                md.stop()
                mt.stop()
                break
        wait(10)
        parar_motor()
        wait(100)

    # Nenhum sensor vê verde
    else:
        print("NÃO TEM VERDE AQUI")
    
    wait(500)


# Lógica de interseção preta
def executar_preto():
    print("É PRETO — Executando lógica normal de interseção preta")
    parar_motor()
    wait(00)
    testtsensor()
    wait(500)
    parar_motor()
    wait(50)
    mov()
    wait(10)
    print("DEU CERTO")