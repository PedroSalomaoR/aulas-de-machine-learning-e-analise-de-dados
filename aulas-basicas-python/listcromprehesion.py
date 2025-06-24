#Aula de list Comprehesion
kmh = [
    40, 50, 56, 70, 80, 89, 96, 100, 120
]

#funciona da mesma forma do map, mas ele já vem em formato de lista
#estrutura: variavel [elemento (função) valor pelo que o elemento vai ser utilizado na função for elemento(ele varre todos os elementos) in lista]
mph3 = [x*0.621371 for x in kmh]
print(mph3)

#outro exemplo
#essa linha cria uma lista com cada caracter da string separado por ''. 
caracteres = [i for i in 'Pedro Salomão']
print(caracteres)