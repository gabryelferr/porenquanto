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
VELOCIDADE_BASE = 120  # Velocidade padrão



def recuadinha():
    velocidade = 100  # Velocidade dos motores
    tempo = 700  # Tempo de movimento em milissegundos (simulando millis())

    # Iniciando o cronômetro
    stopwatch = StopWatch()
    
    # Inicia os motores ao mesmo tempo
    md.run(-velocidade)  # Motor Direito
    mt.run(-velocidade)  # Motor Esquerdo
   
    
    # Aguarda até que o tempo especificado tenha passado
    while stopwatch.time() < tempo:
        pass  # Aguarda até o tempo passar (sem bloquear outras execuções)

    # Após o tempo, para o movimento
    md.stop()
    mt.stop()


def mov():
    pretinho = 40
    mover_para_frente()
    wait(50)
    parar_motor()
    wait(1000)

    print("Verificando à direita primeiro...")
    relogio = StopWatch()
    relogio.reset()

    me.run(-150)
    md.run(-150)
    mt.run(-150)

    while relogio.time() < 300:
        if sensor_direito.reflection() < pretinho:
            print("Sensor direito encontrou preto imediatamente!")
            me.stop()
            md.stop()
            mt.stop()
            break
        wait(10)


    relogio = StopWatch()
    relogio.reset()

    me.run(255)
    md.run(255)
    mt.run(255)

    while relogio.time() < 990:
        if sensor_esquerdo.reflection() < pretinho:
            print("Sensor esquerdo encontrou preto!")
            break
        wait(1000)

   # === Etapa 3: Se não encontrou preto à esquerda, gira pra direita até achar com o direito
    if sensor_esquerdo.reflection() >= pretinho:
        print("Não encontrou preto à esquerda, virando para a direita...")

        me.run(-150)
        md.run(-150)
        mt.run(-150)

        while True:
            if sensor_direito.reflection() < pretinho:
                print("Sensor direito encontrou preto!")
                md.run(-200)
                mt.run(-200)
                wait(500)
                break
            wait(10)

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
    tempo = 1550  # Tempo de movimento em milissegundos (simulando millis())

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
             wait(00)
             testtsensor()
             wait(500)
             parar_motor()
             wait(50)
             mov()
             wait(10)
             print("dDEU CERTO")

        # Seguir em linha reta
        elif se > LIMIAR_PRETO and sd > LIMIAR_PRETO:
            definir_velocidade(md, VELOCIDADE_BASE)
            definir_velocidade(me, -VELOCIDADE_BASE)
            mt.run(0)  # Manter reta

        # Curva para direita
        elif se > LIMIAR_PRETO and sd <= LIMIAR_PRETO:
            definir_velocidade(md, -150)
            definir_velocidade(me, -270)
            mt.run(-270)

        # Curva para esquerda
        elif se <= LIMIAR_PRETO and sd > LIMIAR_PRETO:
            definir_velocidade(md, 150)
            definir_velocidade(me, 270)
            mt.run(270)

        # elif se == LIMIAR_PRETO and sd > LIMIAR_PRETO:
        #     parar_motor()
        #     wait(100)
        #     movf()
        #     parar_motor()
        #     girarateque()

        wait(50)  # Pequeno atraso para estabilidade
seguir_linha()



while True:
    cor_esq = sensor_esquerdo.color()
    cor_dir = sensor_direito.color()

    if cor_esq == ColorSensor.RED or cor_dir == ColorSensor.RED:
        parar_tudo()
        break  # Sai do loop (pode remover o break se quiser continuar monitorando)

    wait(10)
