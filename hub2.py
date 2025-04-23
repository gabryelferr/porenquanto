from pybricks.hubs import PrimeHub
from pybricks.pupdevices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait

hub = PrimeHub()
sensor_frente = UltrasonicSensor(Port.E)

while True:
    dist_frente = sensor_frente.distance() / 10  # Atualiza a cada ciclo

    if 13 < dist_frente <= 30:
        hub.ble.broadcast("VIU OBS")  # envia mensagem
        print(f"Distância: {dist_frente:.1f} cm")
        wait(500)  # Aguarda 0.5s

    elif dist_frente <= 13:
        print(f"Distância mínima com garra")
        wait(800)
    else:
        #hub.ble.broadcast("LIVRE")  # envia outra mensagem
        print(f"Distância segura: {dist_frente:.1f} cm")
        break

    # dist_frente > 50:
        #hub.ble.broadcast("OK")
        #print("para")

        #wait(100)

#     distancia = sensor.distance() / 10  # Converte mm para cm
     

#     if distancia < 8:
#         hub.ble.broadcast(("VIU OBS"))  # envia sinal de parada

#     else:
#         hub.ble.broadcast(("PARAR"))  # envia sinal padrão

#     wait(100)