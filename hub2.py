from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.pupdevices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait
  

hub = PrimeHub(broadcast_channel=125)

sensor_frente = UltrasonicSensor(Port.E)
mg = Motor(Port.F)

while True:
    
#     dist_frente = sensor_frente.distance() / 10  # Atualiza a cada ciclo
    

#     if dist_frente < 30:
#         hub.ble.broadcast("CUIDADO")  # envia mensagem
#         print(f"Distância: {dist_frente:.1f} cm")
#         wait(2000)  # Aguarda 2s
#         mg.run(-450)
#         mg.stop
#         wait(10000)
#         mg.run(450)
#         mg.stop
    
    
#     else:
#         hub.ble.broadcast("LIVRE")  # envia outra mensagem
#         print(f"Distâ ncia segura: {dist_frente:.1f} cm")

#     wait(500)



#     # dist_frente > 50:
#         #hub.ble.broadcast("OK")
#         #print("para")

#         #wait(100)

#     distancia = sensor.distance() / 10  # Converte mm para cm
     

#     if distancia < 8:
#         hub.ble.broadcast(("VIU OBS"))  # envia sinal de parada

#     else:
#         hub.ble.broadcast(("PARAR"))  # envia sinal padrão

#     wait(100)



# hub = PrimeHub()

# def esta_subindo_rampa(limite=10):
#     # Obtém os ângulos de inclinação: [pitch, roll, yaw]
#     pitch, roll, yaw = hub.tilt()

#     print("Inclinação Y (Pitch):", pitch)

#     if pitch > limite:
#         print("Subindo rampa detectada!")
#         return True
#     return False

# # Exemplo de uso
# while True:
#     if esta_subindo_rampa(10):
#         # Exemplo: tomar alguma ação específica
#         print("Executando lógica de rampa")
#         wait(2000)  # Espera para não repetir
#     wait(100)



