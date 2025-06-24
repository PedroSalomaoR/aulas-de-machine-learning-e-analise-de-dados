#transformando listas FLOAT em INT
x = [1,2,3,4]

#teste
for item in x:
    y=float(item)
print(y)    
    
#correção
x2=[2,4,10,6]
nova=[]    
for i in x2:
    nova.append(float(i)) 
print(nova)