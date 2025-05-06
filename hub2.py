from pybricks.hubs import PrimeHub
from pybricks.pupdevices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait

hub = PrimeHub(broadcast_channel=125)

sensor_frente = UltrasonicSensor(Port.E)

while True:
    dist_frente = sensor_frente.distance() / 10  # Atualiza a cada ciclo
    

    if dist_frente < 20:
        hub.ble.broadcast("CUIDADO")  # envia mensagem
        print(f"Distância: {dist_frente:.1f} cm")
        wait(500)  # Aguarda 0.5s
    
    
    else:
        hub.ble.broadcast("LIVRE")  # envia outra mensagem
        print(f"Distâ ncia segura: {dist_frente:.1f} cm")
        
    wait(500)



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