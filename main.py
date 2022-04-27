import os

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))

os.system('clear')


if (a < b+c and b < a+c and c < a+b):
  
  if(a == b and a == c and b == a and b ==c and c == a and b == c):
    print("É um triangulo Equilátero")
  elif(a == b or a == c or b == a or b ==c or c == a or b == c):
    print("É um triangulo Isósceles")
  elif(a != b or a != c or b != a or b !=c or c != a or b != c):
    print("É um triangulo Escaleno")
    
else:
  print("NÃO É UM TRIANGULO")