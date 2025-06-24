#aula sobre a função map
kmh = [
    40, 50, 56, 70, 80, 89, 96, 100, 120
]

#outra possibilidade
mph=[]
for i in kmh:
    y= float(i)
    mph.append(y * 0.621371)

print(mph)

#função map é uma mistura entre função e lista ou tupla
# estrutura: variavel = list se estiver montando uma lista, tuple se estiver montando uma tupla(map(função, lista ou tupla))
mph2= list(map(lambda x: x * 0.621371, kmh))
print(mph2)