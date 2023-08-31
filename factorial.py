print ("Ingrese el numero del factorial a calcular")
num = int(input())
a=1
for i in range(1, num+1):
    a*=i
print("El factorial del numero", num, "es: ", a)