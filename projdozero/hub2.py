from pybricks.hubs import PrimeHub
from pybricks.pupdevices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait
hub = PrimeHub(broadcast_channel=125)


sensor = UltrasonicSensor(Port.A)

while True:
    distancia = sensor.distance() / 10  # Converte mm para cm
    print(f"Distância: {distancia} cm")

    if distancia < 15:
        hub.ble.broadcast(("VIU OBS"))  # envia sinal de parada

    else:
        hub.ble.broadcast(("PARAR"))  # envia sinal padrão

    wait(100)