from pybricks.hubs import PrimeHub
from pybricks.pupdevices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait
hub = PrimeHub(broadcast_channel=125)
hub2 = PrimeHub(observe_channels=[135])

sensor_frente = UltrasonicSensor(Port.C)

comando = hub.ble.observe(135)
dist_frente = sensor_frente.distance() / 10

while True:
        if dist_frente < 14:
            hub.ble.broadcast("VIU OBS")
            wait(500)
        
        else:
            hub.ble.broadcast("OK")

        wait(100)

        if comando:
            print("Comando recebido:", comando)
            if comando == "PARARTUDO":
                 break

# while True:
#     distancia = sensor.distance() / 10  # Converte mm para cm
#     print(f"Distância: {distancia} cm")

#     if distancia < 8:
#         hub.ble.broadcast(("VIU OBS"))  # envia sinal de parada

#     else:
#         hub.ble.broadcast(("PARAR"))  # envia sinal padrão

#     wait(100)