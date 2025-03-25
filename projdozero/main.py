from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait, StopWatch
# from pybricks.media.ev3dev import Sound

# INICIALIZAÇÃO DOS MOTORES E SENSORES
sensor_esquerdo = ColorSensor(Port.C)
sensor_direito = ColorSensor(Port.A)
senaoraux = ColorSensor(Port.E)

me = Motor(Port.D)  # Motor Esquerdo
md = Motor(Port.B)  # Motor Direito
mt = Motor(Port.F)  # Motor Adicional (se necessário)

# # sound = Sound()  # Para emitir sons

# VALORES DE REFLEXÃO
LIMIAR_PRETO = 20  # Ajuste conforme necessário
PP = 50
VELOCIDADE_BASE = 150  # Velocidade padrão


def mov():
    mover_para_frente()
    wait(50)
    parar_motor()
    wait(1000)

    relogio = StopWatch()
    relogio.reset()
    me.run(150)
    md.run(150)
    mt.run(150)

    while relogio.time() < 1080:
        if sensor_esquerdo.reflection() < 50:
            print("Sensor esquerdo encontrou preto!")
            parar_motor()
        wait(1000)

    if sensor_esquerdo.reflection() >= 60:
        print("Não encontrou preto à esquerda, virando para a direita...")

        me.run(-150)
        md.run(-150)  
        mt.run(-150)
        while True:
            if sensor_direito.reflection() <= 60:
                print("Sensor direito encontrou preto!")
                parar_motor()
            wait(2000)

    # === Parar os motores ao final
    me.stop()
    md.stop()
        


def parar_motor():
    """Função para parar todos os motores."""
    me.stop()
    md.stop()
    mt.stop()


# def verifblack():
#     tempo = StopWatch()
#     tempo.reset()

#     while sensor_esquerdo () > LIMIAR_PRETO and tempo.time < 2500:
#         girar(2)
#         wait(10)

#     # === Etapa 2: Verifica se sensor C viu preto ===
#     if sensor_esquerdo() < LIMIAR_PRETO:
#         parar_motor()
#     else:
#         # === Etapa 3: Gira para direita até sensor A ver preto ===
#         while sensor_direito() > LIMIAR_PRETO:
#             girar(150, 1440)
            
#             wait(10)
            

    # tempo_max = 2500  # milissegundos
    # cronometro = StopWatch()
    # se = sensor_esquerdo.reflection()
   

    # # Inicia rotação para esquerda no próprio eixo
    # girar(150,1400)

    # cronometro.reset()
    # while se > LIMIAR_PRETO:
    #     while cronometro.time() < tempo_max:
    #         girar(150,50)
    #     break

        
    # # while se <= LIMIAR_PRETO or cronometro.time() < tempo_max:
    # #     girar(150,50)

    # if se < LIMIAR_PRETO:
    #     parar_motor()
    #     wait(1000)
    #     print("preto")

    # elif se > LIMIAR_PRETO:
    #     girar(-800,1000)
    #     parar_motor()
    #     wait(2000)
    #     print("branco")

def testtsensor():
    st = senaoraux.reflection()
    if st < LIMIAR_PRETO: 
     print("PRETO PEGANDO!")

    else: 
     print("TA VENDO BRANCO!")
                
                
    if sensor_direito.reflection() < LIMIAR_PRETO and sensor_esquerdo.reflection() < LIMIAR_PRETO and senaoraux.reflection() < LIMIAR_PRETO:
     print("INTERSECÇÃO")


def girar(velocidade, tempo):

    stopwatch = StopWatch()
    
    # Inicia os motores ao mesmo tempo
    md.run(velocidade)  # Motor Direito
    me.run(velocidade)  # Motor Esquerdo
   
    # Motor traseiro auxilia na rotação
    mt.run(velocidade)  
    
    # Aguarda até que o tempo especificado tenha passado
    while stopwatch.time() < tempo:
        pass  # Aguarda até o tempo passar (sem bloquear outras execuções)

    # Após o tempo, para o movimento
    parar_motor()

    wait(100)  # Pequeno atraso para estabilizar


def definir_velocidade(motor, velocidade):
    """Define a velocidade de um motor específico."""
    motor.run(velocidade)
    

def mover_para_frente():
    velocidade = 100  # Velocidade dos motores
    tempo = 1650  # Tempo de movimento em milissegundos (simulando millis())

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


def seguir_linha():
    """Função principal para seguir a linha."""
    while True:
        se = sensor_esquerdo.reflection()
        sd = sensor_direito.reflection()
        st = senaoraux.reflection()
        print(senaoraux.reflection())

        # Condição do obstáculo
        if se < LIMIAR_PRETO and sd < LIMIAR_PRETO:
             parar_motor()
             wait(500)
             testtsensor()
             wait(500)
             parar_motor()
             wait(500)
             mov()
            
            # parar_motor()
            # mover_para_frente()
            # wait(500)
            # verifblack()
            # parar_motor()
            # wait(1000)

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
seguir_linha()
