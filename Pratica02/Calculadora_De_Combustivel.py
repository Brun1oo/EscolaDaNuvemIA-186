#Informações sobre a distancia percorrida e combustivel gasto
distancia_percorrida = 300 
combustivel_gasto = 25

#Calculo de consumo medio
consumo_medio = distancia_percorrida / combustivel_gasto

#Exibição para o usuário 
print(f"A distância percorrida do veiculo foi {distancia_percorrida}Km")
print(f"O combustivel gasto foi {combustivel_gasto}L")
print(f"O consumo medio do carro é de {consumo_medio: .2f}")