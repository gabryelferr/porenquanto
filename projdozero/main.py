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


LIMIAR_PRETO = 35
PP = 50
VELOCIDADE_BASE = 160


def moverretao():
    me.run(-500)
    md.run(500)
    wait(10000)


def nove(): 
    me.run(200)
    md.run(200)
    mt.run(200)
    wait(1600)

def novd(): 
    me.run(-200)
    md.run(-200)
    mt.run(-200)
    wait(1600)



def executar_verde():
    parar_motor()
    hub.speaker.beep(1000, 700)
    wait(500)
    variavel_verde = 0
    print("É VERDE — Executando lógica especial")

    me.run(-100)
    md.run(100)
    mt.run(0)
    wait(50)
    parar_motor()
    wait(100)

    esq_verde = detectar_verde(sensor_esquerdo)
    dir_verde = detectar_verde(sensor_direito)

    if esq_verde and dir_verde:
        hub.speaker.beep(800, 700)
        variavel_verde = 3
        print("VERDE NOS DOIS SENSORES")
        me.run(-100)
        md.run(100)
        mt.run(0)
        wait(1300)
        parar_motor()
        novd()
        parar_motor()
        wait(100)
        novd()
        parar_motor()
        wait(100)

    elif esq_verde: 
        variavel_verde = 2
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


    else:
        print("NÃO TEM VERDE AQUI")
    
    wait(500)

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


def recuadinha():
    velocidade = 100
    tempo = 700

    stopwatch = StopWatch()
    
    md.run(-velocidade)
    mt.run(-velocidade)
   
    while stopwatch.time() < tempo:
        pass
    md.stop()
    mt.stop()


def mov():
    pretinho = 40
    mpf_preto()
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

    me.run(265)
    md.run(265)
    mt.run(265)

    while relogio.time() < 990:
        if sensor_esquerdo.reflection() < pretinho:
            print("Sensor esquerdo encontrou preto!")
            break
        wait(1000)

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


def mpf_preto():
    velocidade = 100  # Velocidade dos motores
    tempo = 1480  # Tempo de movimento em milissegundos (simulando millis())

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
        main_to_sec()
        data = hub.ble.observe(125)
        if not(data == None):
            print(data)
            if data == "VIU OBS":
                parar_motor()

        # Verifica se viu vermelho em HSV
        if detectar_vermelho(sensor_direito or sensor_esquerdo):
            print("VERMELHO DETECTADO - PARANDO PARA SEMPRE!")
            parar_motor()
            break  # Sai do loop
    
        se = sensor_esquerdo.reflection()
        sd = sensor_direito.reflection()
        st = senaoraux.reflection()


        # # Condição do obstáculo
        # if se < LIMIAR_PRETO and sd < LIMIAR_PRETO:
        #      parar_motor()
        #      wait(00)
        #      testtsensor()
        #      wait(500)
        #      parar_motor()
        #      wait(50)
        #      mov()
        #      wait(10)
        #      print("dDEU CERTO")

        if se < LIMIAR_PRETO and sd < LIMIAR_PRETO:
            print("OS DOIS SENSORES VIRAM PRETO — VERIFICANDO HSV...")

            if detectar_preto(sensor_esquerdo) and detectar_preto(sensor_direito):
                print("É O BLACK")
                executar_preto()

            elif detectar_verde(sensor_esquerdo) or detectar_verde(sensor_direito):
                print("É O GREEN")
                executar_verde()

        # Seguir em linha reta
        elif se > LIMIAR_PRETO and sd > LIMIAR_PRETO:
            definir_velocidade(md, VELOCIDADE_BASE)
            definir_velocidade(me, -VELOCIDADE_BASE)
            mt.run(0)  # Manter reta

        # Curva para direita
        elif se > LIMIAR_PRETO and sd <= LIMIAR_PRETO:
            definir_velocidade(md, -200)
            definir_velocidade(me, -290)
            mt.run(-295)

        # Curva para esquerda
        elif se <= LIMIAR_PRETO and sd > LIMIAR_PRETO:
            definir_velocidade(me, 200)
            definir_velocidade(md, 290)
            mt.run(295)


        wait(50)  # Pequeno atraso para estabilidade
seguir_linha()
