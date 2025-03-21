from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait, StopWatch
# from pybricks.media.ev3dev import Sound

# INICIALIZAÇÃO DOS MOTORES E SENSORES
sensor_esquerdo = ColorSensor(Port.C)
sensor_direito = ColorSensor(Port.A)

me = Motor(Port.D)  # Motor Esquerdo
md = Motor(Port.B)  # Motor Direito
mt = Motor(Port.F)  # Motor Adicional (se necessário)

# sound = Sound()  # Para emitir sons
timer = StopWatch()  # Temporizador

# VALORES DE REFLEXÃO
LIMIAR_PRETO = 20  # Ajuste conforme necessário
VELOCIDADE_BASE = 160  # Velocidade padrão


def parar_motor():
    """Função para parar todos os motores."""
    me.stop()
    md.stop()
    mt.stop()

# Função para girar 90° à esquerda
def g90e():
    velocidade = 400  # Ajuste a velocidade conforme necessário
    angulo = 90

    # Motores dianteiros giram em direções opostas
    md.run_angle(velocidade, angulo)  
    me.run_angle(velocidade, angulo)

    # Motor traseiro auxilia na rotação
    mt.run_angle(velocidade, angulo)  

    wait(100)  # Pequeno atraso para estabilizar

def g90d():
    velocidade = -200  # Ajuste a velocidade conforme necessário
    angulo = 90

    # Motores dianteiros giram em direções opostas
    md.run_angle(velocidade, angulo)  
    me.run_angle(velocidade, angulo)

    # Motor traseiro auxilia na rotação
    mt.run_angle(velocidade, angulo)  

    wait(100)  # Pequeno atraso para estabilizar

def definir_velocidade(motor, velocidade):
    """Define a velocidade de um motor específico."""
    motor.run(velocidade)
    

def mover_para_frente():
    velocidade = 160  # Velocidade dos motores
    tempo = 2000  # Tempo de movimento em milissegundos (simulando millis())

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



def verificar_sensor():
    return sensor_esquerdo.reflection() < 20  # Retorna True se a reflexão for menor que 20 (detectando preto)


# Função principal para girar 80 graus e verificar o sensor esquerdo
def giro_com_verificacao():
    
    velocidad = 160  # Velocidade dos motores
    temp = 2000  # Tempo de movimento em milissegundos (simulando millis())

    # Iniciando o cronômetro
    stopwatch = StopWatch()
    
    # Inicia os motores ao mesmo tempo
    md.run(velocidad)  # Motor Direito
    me.run(-velocidad)  # Motor Esquerdo
   
    
    # Aguarda até que o tempo especificado tenha passado
    while stopwatch.time() < temp:
        pass  # Aguarda até o tempo passar (sem bloquear outras execuções)

    # Após o tempo, para o movimento
    
    parar_motor()
    wait(5000)

    # # Verifica se o sensor esquerdo encontrou a cor preta
    # if not verificar_sensor():  # Se o sensor esquerdo não detectar preto
    #     print("Sensor esquerdo não detectou preto, voltando para a direita.")
        
    #     # Volta até o sensor da direita detectar preto
    #     while sensor_direito.reflection() >= 20:
    #         g90d()

    #     print("Sensor direito detectou preto. Parando.")
    #     md.stop()
    #     me.stop()
    #     mt.stop()
    # wait(500)
    
    # mover_para_frente(-200, 5.3)
    # timer.reset()


    g90d()
    if sensor_direito.reflection() <= 20:
        md.stop()
        me.stop()
        mt.stop()
        wait(3000)


def seguir_linha():
    """Função principal para seguir a linha."""
    while True:
        se = sensor_esquerdo.reflection()
        sd = sensor_direito.reflection()

        # Condição do obstáculo
        if se < LIMIAR_PRETO and sd < LIMIAR_PRETO:
            parar_motor()
            wait(100)
            mover_para_frente()
            wait(100)
            giro_com_verificacao()

        # Seguir em linha reta
        elif se > LIMIAR_PRETO and sd > LIMIAR_PRETO:
            definir_velocidade(md, VELOCIDADE_BASE)
            definir_velocidade(me, -VELOCIDADE_BASE)
            mt.run(0)  # Manter reta

        # Curva para direita
        elif se > LIMIAR_PRETO and sd <= LIMIAR_PRETO:
            definir_velocidade(md, -160)
            definir_velocidade(me, -280)
            mt.run(-280)

        # Curva para esquerda
        elif se <= LIMIAR_PRETO and sd > LIMIAR_PRETO:
            definir_velocidade(md, 160)
            definir_velocidade(me, 280)
            mt.run(280)

        wait(50)  # Pequeno atraso para estabilidade


# CHAMADA DA FUNÇÃO PRINCIPAL
seguir_linha()


