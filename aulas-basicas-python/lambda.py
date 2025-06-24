def SomaQuadrados(a,b):
    SomaQ= a**2 + b**2
    return SomaQ

print(SomaQuadrados(2,3))

#criando uma função lambda
#estrutura: Nome = lambda parametros, parametros : função1 (operador) função2
SomaQuadrados2 = lambda a, b: a**2 + b**2
#no print da lambda sempre deve vir igual ao de uma função normal, com os parametros
print(SomaQuadrados2(2,3))

x = lambda f: f/2
print(x(10))

#criando uma função que faz a conta da média
Media= lambda n1,n2,ar,pex: (n1*0.1) + (n2*0.2) + (ar*0.5) + (pex*0.2)

p=float(input("digite a nota da ac1: "))
e=float(input("digite a nota da ac2: "))
d=float(input("digite a nota da ar:  "))
r=float(input("digite a nota do PEX: "))
print(f'A sua média final é: {Media(p, e, d, r):.2f}')