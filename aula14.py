# variaveis 
velocidade = 300
local_carro = 90

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade_passou_do_ideal = velocidade > RADAR_1
radar_1 = LOCAL_1 - RADAR_RANGE
radar_2 = LOCAL_1 + RADAR_RANGE
radar_multado = local_carro >= (radar_1) and local_carro <= (radar_2) \
and velocidade_passou_do_ideal

if velocidade_passou_do_ideal:
    print("passou do ideal de velocidade")

velocidade_passou_do_ideal = velocidade > RADAR_1
if radar_multado and velocidade_passou_do_ideal:
    print("passou do ideal de velocidade e levou multa")